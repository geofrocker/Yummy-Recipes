"""Yummy recipes app for creating,retrieving,updating and deleting recipes"""
import os
from functools import wraps
import uuid
from datetime import datetime
from flask import Flask, render_template, flash, redirect, url_for, session, request
from wtforms import Form, StringField, BooleanField, TextAreaField, SelectField, PasswordField, validators
from recipes import recipes
from data import Recipe, User, Category, Review, UpVote


app = Flask(__name__)

all_recipes = recipes()
new_recipe = Recipe()
user = User()
category = Category()
review = Review()
upVote = UpVote()
#All Recipes
@app.route('/')
def recipes():
    """Display all recipes"""
    new_recipes=new_recipe.get_recipes()
    for recipe in new_recipes:
        reviews = review.get_num_reviews(recipe['id'])
        votes = upVote.get_upVotes(recipe['id'])
        recipe['votes'] = votes
        recipe['reviews'] = reviews
    if all_recipes:
        return render_template('recipes.html', all_recipes=all_recipes, new_recipes=new_recipes)
    else:
        msg = 'No Recipes Found'
        return render_template('recipes.html', msg=msg)

#Review form class
class ReviewForm(Form):
    """Review form"""
    review = TextAreaField(u'Review', validators=[validators.Length(min=2)])

#Register form class
class RegisterForm(Form):
    """Register form for new users"""
    name = StringField(u'Name', validators=[validators.Length(min=1, max=50)])
    username = StringField(u'Username', validators=[validators.Length(min=1, max=50)])
    email = StringField(u'Email', validators=[validators.Length(min=1, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
        ])
    confirm = PasswordField('Confirm Password')

#Recipe form class
class RecipeForm(Form):
    """Recipe form for adding and editing recipes"""
    title = StringField(u'Title', validators=[validators.Length(min=1, max=200)])
    category = SelectField(u'Category', coerce=str)
    ingredients = StringField(u'Ingredients', validators=[validators.Length(min=1, max=200)])
    steps = TextAreaField(u'Steps', validators=[validators.Length(min=10)])
    status = BooleanField(u'Private')

#Category form class
class CategoryForm(Form):
    """Category form"""
    name = StringField(u'Name', validators=[validators.Length(min=3, max=50)])

#user register
@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register function for a new user"""
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = form.password.data
        if user.check_user_name(username):
            flash('Username already taken', 'danger')
            return redirect(url_for('register'))
        if user.check_user_email(email):
            flash('Email already exists', 'danger')
            return redirect(url_for('register'))
        user_data = {'id':str(uuid.uuid4()),'name':name,'email':email,'username':username,'password':password}
        response = user.register_user(user_data)
        #flash message
        flash(response, 'success')
        #redirect to home page
        return redirect(url_for('recipes'))
    return render_template('register.html', form=form)

#user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login function for a member"""
    if request.method == 'POST':
        #get form fields
        username = request.form['username']
        password_candidate = request.form['password']
        logged_in_user = user.login_user(username,password_candidate)
        if logged_in_user:
            #passed
            session['logged_in'] = True
            session['username'] = username
            flash('Your are now logged in', 'success')
            return redirect(url_for('dashboard'))

        else:
            error = 'User not found'
            return render_template('login.html', error=error)
    return render_template('login.html')

#Check if user is logged
def is_logged_in(f):
    """implement decorator for checking if a user is logged in"""
    @wraps(f)
    def wrap(*args, **kwargs):
        """check if user is logged"""
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorised, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

#logout
@app.route('/logout')
@is_logged_in
def logout():
    """log out function for the user"""
    session.clear()
    return redirect(url_for('login'))

#Add category
@app.route('/add_category', methods=['GET', 'POST'])
@is_logged_in
def add_category():
    """Add category function"""
    form = CategoryForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        created_by=session['username']
        if category.get_category_name(created_by, name):
            #flash message
            flash('Category already exists', 'danger')
            #redirect to home page
            return redirect(url_for('add_category'))
        cat_data = {'id':str(uuid.uuid4()), 'name':name, 'created_by':created_by}
        response = category.set_category(cat_data)
        #flash message
        flash(response, 'success')
        #redirect to home page
        return redirect(url_for('dashboard'))
    return render_template('add_category.html', form=form)

#Edit Category
@app.route('/edit_category/<string:cat_id>', methods=['POST', 'GET'])
@is_logged_in
def edit_category(cat_id):
    """Ëdit function for the category"""
    #get form
    form = CategoryForm(request.form)
    #populate form fields
    if category.get_category(cat_id):
        form.name.data=category.get_category(cat_id)

    if request.method == 'POST' and form.validate():
        new_name=request.form['name']
        created_by=session['username']
        cat_data = {'id':cat_id, 'name':new_name, 'created_by':created_by}
        response = category.edit_category(cat_id, cat_data)
        flash(response, 'success')
        return redirect(url_for('dashboard'))

    return render_template('edit_category.html', form=form)

#Delete Category
@app.route('/delete_category/<string:cat_id>', methods=['POST'])
@is_logged_in
def delete_category(cat_id):
    """Delete function for deleting category"""
    response = ''
    if category.get_category(cat_id):
        response = category.delete_category(cat_id)
    flash(response, 'success')
    return redirect(url_for('dashboard'))

#dashboard
@app.route('/dashboard')
@is_logged_in
def dashboard():
    """implement the user dashboard"""
	#get Recipes
    all_recipes=new_recipe.get_user_recipes(session['username'])
    all_categories=category.get_user_categories(session['username'])
    if all_recipes:
        return render_template('dashboard.html', all_recipes=all_recipes, all_categories=all_categories)
    else:
        msg = 'No Recipes Found'
        return render_template('dashboard.html', msg=msg, all_categories=all_categories)

#add recipe
@app.route('/add_recipe', methods=['POST', 'GET'])
@is_logged_in
def add_recipe():
    """Function for adding a recipe"""
    form = RecipeForm(request.form)
    category = Category()
    all_categories=category.get_user_categories(session['username'])
    if all_categories:
        form.category.choices = [(cat['name'], cat['name']) for cat in all_categories]
    else:
        form.category.choices = [('General', 'General')]
    if request.method == 'POST' and form.validate():
        recipe_data = {}
        title = form.title.data
        category = form.category.data
        ingredients = form.ingredients.data
        steps = form.steps.data
        status = form.status.data
        if status:
            private = True
        else:
            private = False
        if session['username']:
            created_by = session['username']
        else:
            created_by = 'Anonymous'
        if new_recipe.get_recipe_titles(created_by, title):
            #flash message
            flash('Title already exists', 'danger')
            #redirect to home page
            return redirect(url_for('add_recipe'))
            
        recipe_data = {'id':str(uuid.uuid4()),'title':title,'category':category,'ingredients':ingredients,'steps':steps,'create_date':datetime.now(),'created_by':created_by,'private':private,'votes':0,'reviews':0}
        response = new_recipe.set_recipe(recipe_data)
        flash(response, 'success')

        return redirect(url_for('dashboard'))

    return render_template('add_recipe.html', form=form)

#Edit recipe
@app.route('/edit_recipe/<string:id>', methods=['POST', 'GET'])
@is_logged_in
def edit_recipe(id):
    """Ëdit function for the recipe"""
    #get form
    form = RecipeForm(request.form)
    data=new_recipe.get_recipe(id)
    category = Category()
    all_categories=category.get_user_categories(session['username'])
    if all_categories:
        form.category.choices = [(cat['name'], cat['name']) for cat in all_categories]
    form.category.choices = [(data['category'], data['category'])]
    #populate form fields
    if new_recipe.get_recipe(id):
        form.title.data=data['title']
        form.ingredients.data=data['ingredients']
        form.steps.data=data['steps']

    if request.method == 'POST' and form.validate():
        title = request.form['title']
        category = request.form['category']
        ingredients = request.form['ingredients']
        steps = request.form['steps']
        private = form.status.data
        if session['username']:
            created_by = session['username']
        else:
            created_by = 'Anonymous'
        recipe_data = {'id':id,'title':title,'category':category,'ingredients':ingredients,'steps':steps,'create_date':datetime.now(),'created_by':created_by,'private':private}
        response = new_recipe.edit_recipe(id,recipe_data)
        flash(response, 'success')
        return redirect(url_for('dashboard'))

    return render_template('edit_recipe.html', form=form)


#Delete Recipe
@app.route('/delete_recipe/<string:id>', methods=['POST'])
@is_logged_in
def delete_recipe(id):
    """Delete function for deleting recipes"""
    response = ''
    if new_recipe.get_recipe(id):
        response = new_recipe.delete_recipe(id)
    flash(response, 'success')
    return redirect(url_for('dashboard'))

#Review Recipe
@app.route('/recipe/<string:id>', methods=['GET','POST'])
@is_logged_in
def recipe(id):
    """Display all recipes"""
    recipe = new_recipe.get_recipe(id)
    reviews = review.get_reviews(id)
    votes = upVote.get_upVotes(id)
    form = ReviewForm(request.form)
    if recipe:
        if request.method == 'POST' and form.validate():
            review_data = {}
            user_review = form.review.data
            created_by = session['username']
            create_date = datetime.now()
            review_data = {'id':str(uuid.uuid4()), 'recipe_id':id, 'review':user_review, 'created_by':created_by, 'create_date':create_date}
            response = review.set_review(review_data)
            #flash message
            flash(response, 'success')
            #redirect to review page
            return redirect(url_for('recipe', id=id))
        return render_template('review.html', recipe=recipe, all_reviews=reviews, votes=votes, form=form)
    else:
        msg = 'Recipe not Found'
        return render_template('review.html', msg=msg)

#Up vote Recipe
@app.route('/up_vote/<string:id>', methods=['POST'])
@is_logged_in
def up_vote(id):
    """Up_vote function for upvoting recipes"""
    upvote_data = {'id':str(uuid.uuid4()),'recipe_id':id,'voted_by':session['username']}
    if upVote.check_upvote(session['username'], id):
        #flash message
        flash('You already upvoted this recipe', 'success')
        #redirect to review page
        return redirect(url_for('recipe', id=id))
    response = upVote.set_upvote(upvote_data)
    flash(response, 'success')
    return redirect(url_for('recipe', id=id))

app.secret_key = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
if __name__ == '__main__':
    app.run(debug=True)
    app.run()