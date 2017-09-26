from flask import Flask,render_template,flash,redirect,url_for,session,request
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from functools import wraps
from recipes import recipes
app=Flask(__name__)
usernames = []
emails = []
passwords = []
all_recipes=recipes()
#All Recipes
@app.route('/')
def recipes():
    if all_recipes:
	    return render_template('recipes.html',all_recipes=all_recipes)
    else:
        msg='No Recipes Found'
        return render_template('recipes.html',msg=msg)

#Register form class
class RegisterForm(Form):
    name = StringField(u'Name', validators=[validators.Length(min=1,max=50)])
    username = StringField(u'Username', validators=[validators.Length(min=1,max=50)])
    email  = StringField(u'Email', validators=[validators.Length(min=1,max=50)])
    password = PasswordField('Password',[
    	validators.DataRequired(),
    	validators.EqualTo('confirm',message='Passwords do not match')
    	])
    confirm = PasswordField('Confirm Password')

#user register
@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.method=='POST' and form.validate():
        name=form.name.data 
        email=form.email.data 
        username=form.username.data 
        password=form.password.data
        usernames.append(username)
        emails.append(email)
        passwords.append(password)
        #flash message
        flash('Your are now registered and can log in','success')
        #redirect to home page
        redirect(url_for('recipes'))
    return render_template('register.html',form=form)

#user login
@app.route('/login', methods =['GET','POST'])
def login():
    if request.method == 'POST':
        #get form fields
        username=request.form['username']
        password_candidate=request.form['password']

        if username in usernames and password_candidate in passwords:
            #passed
            session['logged_in']=True
            session['username']=username
            flash('Your are now logged in','success')
            return redirect(url_for('dashboard'))

        else:
            error='User not found'
            return render_template('login.html',error=error)
    return render_template('login.html')

#Check if user is logged
def is_logged_in(f):
	@wraps(f)
	def wrap(*args,**kwargs):
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
	session.clear()
	flash('You are now logged out','success')
	return redirect(url_for('login'))

@is_logged_in
@app.route('/dashboard') 
def dashboard():
	
	#get Recipes
	if all_recipes:
		return render_template('dashboard.html',all_recipes=all_recipes)
	else:
		msg='No Recipes Found'
		return render_template('dashboard.html',msg=msg)

#Recipe form class
class RecipeForm(Form):
    title = StringField(u'Title', validators=[validators.Length(min=1,max=200)])
    ingredients = StringField(u'Ingrdients', validators=[validators.Length(min=1,max=200)])
    steps = TextAreaField(u'Body', validators=[validators.Length(min=30)])
    
#add recipe
@app.route('/add_recipe', methods=['POST','GET'])
@is_logged_in 
def add_recipe():
	form = RecipeForm(request.form)
	if request.method=='POST' and form.validate():
		
		flash('Cannot create Recipe at the moment','success')

		return redirect(url_for('dashboard'))

	return render_template('add_recipe.html',form=form)

#Edit recipe
@app.route('/edit_recipe/<string:id>', methods=['POST','GET'])
@is_logged_in 
def edit_recipe(id):
	#get form
	form = RecipeForm(request.form)

	if request.method=='POST' and form.validate():
		title=request.form['title']
		body=request.form['body']

		flash('Cannot create recipe at the moment','success')

		return redirect(url_for('dashboard'))

	return render_template('edit_recipe.html',form=form)


#Delete Recipe
@app.route('/delete_recipe/<string:id>', methods=['POST'])
@is_logged_in 
def delete_recipe(id):
	
	flash('Cannot delete recipe at the moment','success')

	return redirect(url_for('dashboard'))

if __name__=='__main__':
	app.secret_key='secret123'
	app.run(debug=True)