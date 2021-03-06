"""Yummy recipes app for creating,retrieving,updating and deleting recipes"""
import os
from functools import wraps
import random
from datetime import datetime
from flask import Flask, render_template, flash, redirect, url_for, session, request
from wtforms import Form, StringField, TextAreaField, SelectField, PasswordField, validators
from recipes import recipes
from recipenew import Recipe,User,Category


app = Flask(__name__)

all_recipes = recipes()
new_recipe=Recipe()
user=User()
category=Category()
#All Recipes
@app.route('/')
def recipes():
    """Display all recipes"""
    if all_recipes:
        return render_template('recipes.html', all_recipes=all_recipes, new_recipes=new_recipe.get_recipe())
    else:
        msg = 'No Recipes Found'
        return render_template('recipes.html', msg=msg)

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

#Category form class
class CategoryForm(Form):
    """Category form"""
    name = StringField(u'Name', validators=[validators.Length(min=3, max=50)])

#Add category
@app.route('/add_category', methods=['GET', 'POST'])
def add_category():
    """Add category function"""
    form = CategoryForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        category.set_category(name)
        #flash message
        flash('Category created successfully', 'success')
        #redirect to home page
        return redirect(url_for('dashboard'))
    return render_template('add_category.html', form=form)

#Edit Category
@app.route('/edit_category/<string:name>', methods=['POST', 'GET'])
def edit_category(name):
    """Ëdit function for the category"""
    #get form
    form = CategoryForm(request.form)
    #populate form fields
    if category.get_category(name)== name:
        form.name.data=category.get_category(name)

    if request.method == 'POST' and form.validate():
        newname=request.form['name']
        category.edit_category(name,newname)
        flash('Category edited successfully', 'success')
        return redirect(url_for('dashboard'))

    return render_template('edit_category.html', form=form)

#Delete Category
@app.route('/delete_category/<string:name>', methods=['POST'])
def delete_category(name):
    """Delete function for deleting category"""
    if category.get_category(name) == name:
        category.delete_category(name)
    flash('Recipe deleted Successfully', 'success')
    return redirect(url_for('dashboard'))

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
        user.set_user(name,username,email,password)
        #flash message
        flash('Your are now registered and can log in', 'success')
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

        if user.get_username()==username and user.get_password()==password_candidate:
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

#dashboard
@app.route('/dashboard')
@is_logged_in
def dashboard():
    """implement the user dashboard"""
	#get Recipes
    if new_recipe.get_recipe():
        return render_template('dashboard.html', all_recipes=new_recipe.get_user_recipe(),all_categories=category.get_categories())
    else:
        msg = 'No Recipes Found'
        return render_template('dashboard.html', msg=msg)

#Recipe form class
class RecipeForm(Form):
    """Recipe form for adding and editing recipes"""
    title = StringField(u'Title', validators=[validators.Length(min=1, max=200)])
    category = SelectField(u'Category', coerce=str)
    ingredients = StringField(u'Ingredients', validators=[validators.Length(min=1, max=200)])
    steps = TextAreaField(u'Steps', validators=[validators.Length(min=30)])

#add recipe
@app.route('/add_recipe', methods=['POST', 'GET'])
@is_logged_in
def add_recipe():
    """Function for adding a recipe"""
    form = RecipeForm(request.form)
    category=Category()
    all_categories=category.get_categories()
    if all_categories:
        form.category.choices = [(cat, cat) for cat in all_categories]
    form.category.choices = [('General', 'General')]
    if request.method == 'POST' and form.validate():
        title = form.title.data
        category = form.category.data
        ingredients = form.ingredients.data
        steps = form.steps.data
        if session['username']:
            created_by = session['username']
        else:
            created_by = 'Anonymous'
        new_recipe.set_recipe('1',title,category,ingredients,steps,datetime.now(),created_by)
        flash('Recipe created successfully', 'success')

        return redirect(url_for('dashboard'))

    return render_template('add_recipe.html', form=form)

#Edit recipe
@app.route('/edit_recipe/<string:id>', methods=['POST', 'GET'])
@is_logged_in
def edit_recipe(id):
    """Ëdit function for the recipe"""
    #get form
    form = RecipeForm(request.form)
    category=Category()
    all_categories=category.get_categories()
    if all_categories:
        form.category.choices = [(cat, cat) for cat in all_categories]
    form.category.choices = [('General', 'General')]
    #populate form fields
    if new_recipe.get_id() == id:
        form.title.data=new_recipe.get_title()
        form.ingredients.data=new_recipe.get_ingredients()
        form.steps.data=new_recipe.get_steps()

    if request.method == 'POST' and form.validate():
        title=request.form['title']
        cat = request.form['category']
        ingredients=request.form['ingredients']
        steps=request.form['steps']
        if user.get_username():
            created_by = user.get_username()
        else:
            created_by = 'Anonymous'
        new_recipe.set_recipe('1',title,cat,ingredients,steps,datetime.now(),created_by)
        new_recipe.edit_recipe('1',title,cat,ingredients,steps,datetime.now(),created_by)
        flash('Recipe edited successfully', 'success')
        return redirect(url_for('dashboard'))

    return render_template('edit_recipe.html', form=form)


#Delete Recipe
@app.route('/delete_recipe/<string:id>', methods=['POST'])
@is_logged_in
def delete_recipe(id):
    """Delete function for deleting recipes"""
    if new_recipe.get_id() == id:
        new_recipe.set_recipe('','','','','','','',)
    flash('Recipe deleted Successfully', 'success')
    return redirect(url_for('dashboard'))

app.secret_key = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
if __name__ == '__main__':
    app.run(debug=True)
    app.run()