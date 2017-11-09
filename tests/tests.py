"""Test for yummy recipe web app"""
import unittest
from datetime import datetime
from app import app, RecipeForm
from data import Recipe, User, Category, Review, UpVote
from flask import session

class DataTestCase(unittest.TestCase):
    
    def setUp(self):
        app.secret_key = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
        self.recipe = Recipe()
        self.user = User()
        self.category = Category()
        self.review = Review()
        self.upVote = UpVote()
        self.recipe_data = {'id':'5XXXXX', 'title':'Recipe one one', 'category':'General', 'ingredients':'Ingredient one', 'steps':'step onestep one step one', 'create_date':datetime.now(), 'created_by':'Geofrey', 'private':False, 'votes':0, 'reviews':0, 'status':False}
        self.user_data = {'id':'5XXXXX','name':'Geofrey','email':'geofrocker2@gmail.com','username':'Geofrocker','password':'12345', 'confirm':'12345'}
        self.user_data2 = {'id':'5XXXXX','name':'Geofrey','email':'geofrocker3@gmail.com','username':'Geofrocker2','password':'12345', 'confirm':'12345'}
        self.user_data3 = {'id':'5XXXXX','name':'Geofrey','email':'geofrocker2@gmail.com','username':'Geofrocker4','password':'12345', 'confirm':'12345'}
        self.cat_data = {'id':'5XXXXX', 'name':'General', 'created_by':'Geofrocker'}
        self.review_data = {'id':'1XXXXX', 'recipe_id':'5XXXXX', 'review':'Coooool', 'created_by':'Geofrocker', 'create_date':datetime.now()}
        self.upvote_data = {'id':'1XXXXX', 'recipe_id':'5XXXXX','voted_by':'Geofrocker'}

    def test_add_recipe(self):
        '''test add recipe'''
        response = self.recipe.set_recipe(self.recipe_data)
        self.assertEqual(response, "Recipe created successfully", msg = "Can't create recipe")

    def test_edit_recipe(self):
        '''test edit recipe'''
        self.recipe.set_recipe(self.recipe_data)
        response = self.recipe.edit_recipe('5XXXXX', self.recipe_data)
        response2 = self.recipe.edit_recipe('5XERROR', self.recipe_data)
        self.assertEqual(response, "Recipe does not exist", msg = "Can't edit recipe")
        self.assertEqual(response2, "Recipe does not exist", msg = "Can't edit recipe")

    def test_delete_recipe(self):
        '''test delete recipe'''
        self.recipe.set_recipe(self.recipe_data)
        response = self.recipe.delete_recipe('5XXXXX')
        response2 = self.recipe.delete_recipe('5XERROR')
        self.assertEqual(response, "Recipe deleted", msg = "Can't delete recipe")
        self.assertEqual(response2, "Recipe does not exist", msg = "Can't delete recipe")

    def test_get_recipes(self):
        '''test get recipes'''
        response = self.recipe.get_recipes()
        self.assertIsInstance(response, list, msg = "Can't get recipes")
        self.assertIsInstance(response[0], dict, msg = "Can't get recipes")


    def test_get_recipe(self):
        response = self.recipe.get_recipe('5XXXXX')
        self.assertIsInstance(response, dict, msg = "Can't get recipes")

    def get_user_recipes(self):
        '''test get user recipes'''
        response = self.recipe.get_user_recipes('Geofrocker')
        self.assertIsInstance(response, list, msg = "Can't get recipes")
        self.assertIsInstance(response[0], dict, msg = "Can't get recipes")

    def get_recipe_titles(self):
        '''test get recipe titles'''
        response = self.recipe.get_recipe_titles('Geofrocker','Recipe one')
        self.assertIsInstance(response, list, msg = "Can't get recipes")
        self.assertIsInstance(response[0], dict, msg = "Can't get recipes")

    def test_reg_user(self):
        '''test register user'''
        response = self.user.register_user(self.user_data)
        self.assertEqual(response, "Your are now registered and can log in", msg = "Can't create recipe")

    def test_check_user_name(self):
        '''test username check'''
        self.user.register_user(self.user_data)
        response = self.user.check_user_name('Geofrocker')
        self.assertIsInstance(response, list, msg = "Can't get username")
        self.assertIsInstance(response[0], dict, msg = "Can't get username")

    def test_check_user_email(self):
        '''test user email check'''
        self.user.register_user(self.user_data)
        response = self.user.check_user_email('geofrocker2@gmail.com')
        self.assertIsInstance(response, list, msg = "Can't get user email")
        self.assertIsInstance(response[0], dict, msg = "Can't get user email")

    def test_login_user(self):
        '''test user login'''
        response = self.user.login_user('Geofrocker','12345')
        self.assertIsInstance(response, list, msg = "Can't login user")
        self.assertIsInstance(response[0], dict, msg = "Can't login user")

    def test_set_category(self):
        '''test set category'''
        response = self.category.set_category(self.cat_data)
        self.assertEqual(response, "Category created successfully", msg = "Can't create category")

    def test_get_category(self):
        '''test get actegory'''
        self.category.set_category(self.cat_data)
        response = self.category.get_category('5XXXXX')
        self.assertEqual(response, "General", msg = "Can't get category")

    def test_edit_category(self):
        '''test edit category'''
        self.category.set_category(self.cat_data)
        response = self.category.edit_category('5XXXXX',self.cat_data)
        self.assertEqual(response, "Category edited successfully", msg = "Can't edit category")

    def test_delete_category(self):
        '''test delete category'''
        self.category.set_category(self.cat_data)
        response = self.category.delete_category('5XXXXX')
        self.assertEqual(response, "Category deleted Successfully", msg = "Can't delete category")

    def test_get_categories(self):
        '''test get categories'''
        response = self.category.get_categories()
        self.assertIsInstance(response, list, msg = "Can't get categories")
        self.assertIsInstance(response[0], dict, msg = "Can't get categories")

    def test_get_user_categories(self):
        '''test get user categories'''
        response = self.category.get_user_categories('Geofrocker')
        self.assertIsInstance(response, list, msg = "Can't get user categories")
        self.assertIsInstance(response[0], dict, msg = "Can't get user categories")

    def test_get_category_name(self):
        '''test get category name'''
        response = self.category.get_category_name('Geofrocker','General')
        self.assertIsInstance(response, list, msg = "Can't get category name")
        self.assertIsInstance(response[0], dict, msg = "Can't get category name")

    def test_set_review(self):
        '''test set review'''
        response = self.review.set_review(self.review_data)
        self.assertEqual(response, "Review created successfully", msg = "Can't create review")

    def test_get_reviews(self):
        '''test get reviews'''
        self.review.set_review(self.review_data)
        response = self.review.get_reviews('5XXXXX')
        self.assertIsInstance(response, list, msg = "Can't get review")
        self.assertIsInstance(response[0], dict, msg = "Can't get reviews")

    def test_get_num_reviews(self):
        '''test get number of reviews'''
        self.review.set_review(self.review_data)
        response = self.review.get_num_reviews('5XXXXX')
        self.assertIsInstance(response, int, msg = "Can't get number reviews")

    def test_set_upvote(self):
        '''test set upvote'''
        response = self.upVote.set_upvote(self.upvote_data)
        self.assertEqual(response, "Recipe upvoted Successfully", msg = "Can't upvote recipe")

    def test_check_upvote(self):
        '''test check upvotes'''
        self.upVote.set_upvote(self.upvote_data)
        response = self.upVote.check_upvote('Geofrocker','5XXXXX')
        self.assertIsInstance(response, list, msg = "Can't get upvote")
        self.assertIsInstance(response[0], dict, msg = "Can't get upvote")

    def test_get_upVotes(self):
        '''test get number of upvotes'''
        self.upVote.set_upvote(self.upvote_data)
        response = self.upVote.get_upVotes('5XXXXX')
        self.assertIsInstance(response, int, msg = "Can't get votes")

#++++++++++++++++++++++Testing end points++++++++++++++++++++++++++++++++++++++++++++++++++++++

    def test_home_page_header(self):
        """Test home page"""
        client = app.test_client()
        rsp = client.get('/')
        self.assertIn('Recipe one', str(rsp.data))

    def test_login_page_header(self):
        """Test login_page"""
        client = app.test_client(self)
        rsp = client.post('/login', content_type='application/x-www-form-urlencoded', data={'username':'geom','password':'12345'}, follow_redirects=True)
        self.assertIn('User not found', str(rsp.data))
        rsp = client.post('/login', content_type='application/x-www-form-urlencoded', data=self.user_data, follow_redirects=True)
        self.assertIn('Your are now logged in', str(rsp.data))

    def test_logout_header(self):
        """Test dashboard_page"""
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess.clear()
            rsp = c.get('/logout', follow_redirects=True)
            self.assertTrue(rsp, msg='Cant logout')

    def test_register_page_header(self):
        """Test register_page"""
        client = app.test_client(self)
        rsp = client.post('/register', content_type='application/x-www-form-urlencoded', data=self.user_data, follow_redirects=True)
        self.assertIn('Username already taken', str(rsp.data))
        rsp = client.post('/register', content_type='application/x-www-form-urlencoded', data=self.user_data3, follow_redirects=True)
        self.assertIn('Email already exists', str(rsp.data))
        rsp = client.post('/register', content_type='application/x-www-form-urlencoded', data=self.user_data2, follow_redirects=True)
        self.assertIn('Your are now registered and can log in', str(rsp.data))

    def test_dashboard_page_header(self):
        """Test dashboard_page"""
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['username'] = 'Geofrocker'
                sess['logged_in'] = True
            rsp = c.get('/dashboard')
            self.assertIn('Recipe one', str(rsp.data))

    def test_add_recipe_page_header(self):
        """Test edit_recipe_page"""
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['username'] = 'Geofrocker'
                sess['logged_in'] = True
            rsp = c.post('/add_recipe', content_type='application/x-www-form-urlencoded', data=self.recipe_data, follow_redirects=True)
            self.assertIn('Recipe created successfully', str(rsp.data))

    def test_edit_recipe_page_header(self):
        """Test edit_recipe_page"""
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['username'] = 'Geofrocker'
                sess['logged_in'] = True
            rsp = c.post('/edit_recipe/5XXXXX', content_type='application/x-www-form-urlencoded', data=self.recipe_data, follow_redirects=True)
            self.assertIn('Recipe does not exist', str(rsp.data))

    def test_delete_recipe_page_header(self):
        """Test delete_recipe_page"""
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['username'] = 'Geofrocker'
                sess['logged_in'] = True
            rsp = c.post('/delete_recipe/5XXXXX', follow_redirects=True)
            self.assertIn('Recipe does not exist', str(rsp.data))

    def test_add_category_page_header(self):
        """Test add_category_page"""
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['username'] = 'Geofrocker'
                sess['logged_in'] = True
            rsp = c.post('/add_category', content_type='application/x-www-form-urlencoded', data=self.cat_data, follow_redirects=True)
            self.assertIn('Category created successfully', str(rsp.data))

    def test_edit_category_page_header(self):
        """Test edit_category_page"""
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['username'] = 'Geofrocker'
                sess['logged_in'] = True
            rsp = c.post('/edit_category/5XXXXX', content_type='application/x-www-form-urlencoded', data=self.cat_data, follow_redirects=True)
            self.assertIn('Category edited successfully', str(rsp.data))

    def test_delete_category_page_header(self):
        """Test delete_category_page"""
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['username'] = 'Geofrocker'
                sess['logged_in'] = True
            rsp = c.post('/delete_category/1XXXXX', follow_redirects=True)
            self.assertIn('', str(rsp.data))

    def test_add_review_page_header(self):
        """Test add_review_page"""
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['username'] = 'Geofrocker'
                sess['logged_in'] = True
            rsp = c.post('/recipe/5XXXXX', content_type='application/x-www-form-urlencoded', data=self.review_data, follow_redirects=True)
            self.assertIn('Review created successfully', str(rsp.data))

    def test_add_upvote_page_header(self):
        """Test upvote_page"""
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['username'] = 'Geofrocker'
                sess['logged_in'] = True
            rsp = c.post('/up_vote/5XXXXX', content_type='application/x-www-form-urlencoded', data=self.upvote_data, follow_redirects=True)
            self.assertIn('Recipe upvoted Successfully', str(rsp.data))

    

