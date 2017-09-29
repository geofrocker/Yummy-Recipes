"""Yummy recipes app for creating,retrieving,updating and deleting recipes"""
import os
from functools import wraps
import random
from datetime import datetime
from flask import Flask, render_template, flash, redirect, url_for, session, request
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from recipes import recipes
from recipenew import Recipe,User

app = Flask(__name__)

all_recipes = recipes()
new_recipe=Recipe('','','','','','')
user=User('','','','')
#All Recipes
@app.route('/')
def recipes():
    """Display all recipes"""
    if all_recipes:
        return render_template('recipes.html', all_recipes=all_recipes)
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
        redirect(url_for('recipes'))
    return render_template('register.html', form=form)

#user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login function for a member"""
    if request.method == 'POST':
        #get form fields
        username = request.form['username']
        password_candidate = request.form['password']

        if user.get_username() and user.get_password():
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

@is_logged_in
@app.route('/dashboard')
def dashboard():
    """implement the user dashboard"""
	#get Recipes
    if new_recipe.get_recipe():
        return render_template('dashboard.html', all_recipes=new_recipe.get_recipe())
    else:
        msg = 'No Recipes Found'
        return render_template('dashboard.html', msg=msg)

#Recipe form class
class RecipeForm(Form):
    """Recipe form for adding and editing recipes"""
    title = StringField(u'Title', validators=[validators.Length(min=1, max=200)])
    ingredients = StringField(u'Ingredients', validators=[validators.Length(min=1, max=200)])
    steps = TextAreaField(u'Steps', validators=[validators.Length(min=30)])

#add recipe
@app.route('/add_recipe', methods=['POST', 'GET'])
@is_logged_in
def add_recipe():
    """Function for adding a recipe"""
    form = RecipeForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        ingredients = form.ingredients.data
        steps = form.steps.data
        if user.get_username():
            created_by = user.get_username()
        else:
            created_by = 'Anonymous'
        new_recipe.set_recipe(random.randrange(1, 20),title,ingredients,steps,datetime.now(),created_by)
        
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
    #populate form fields
    if new_recipe.get_id() == id:
        form.title.data=new_recipe.get_title()
        form.ingredients.data=new_recipe.get_ingredients()
        form.steps.data=new_recipe.get_steps()

    if request.method == 'POST' and form.validate():
        title=request.form['title']
        ingredients=request.form['ingredients']
        steps=request.form['steps']
        new_recipe.edit_recipe(id,title,ingredients,steps)
        flash('Recipe edited successfully', 'success')
        return redirect(url_for('dashboard'))

    return render_template('edit_recipe.html', form=form)


#Delete Recipe
@app.route('/delete_recipe/<string:id>', methods=['POST'])
@is_logged_in
def delete_recipe(id):
    """Delete function for deleting recipes"""
    if new_recipe.get_id() == id:
        new_recipe.set_recipe('','','','','','',)
    flash('Recipe deleted Successfully', 'success')
    return redirect(url_for('dashboard'))

app.secret_key = os.urandom(24)
if __name__ == '__main__':
    app.run(debug=True)
    app.run()
