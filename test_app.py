"""Test for yummy recipe web app"""
from app import app

def test_home_page_header():
    client = app.test_client()
    rsp = client.get('/')
    assert rsp.status == '200 OK'

def test_login_page_header():
    client = app.test_client()
    rsp = client.get('/login')
    assert rsp.status == '200 OK'

def test_register_page_header():
    client = app.test_client()
    rsp = client.get('/register')
    assert rsp.status == '200 OK'

def test_dashboard_page_header():
    client = app.test_client()
    rsp = client.get('/dashboard')
    assert rsp.status == '200 OK'
    
def test_add_recipe_page_header():
    client = app.test_client()
    rsp = client.post('/add_recipe')
    assert rsp.status == '500 INTERNAL SERVER ERROR'

def test_edit_recipe_page_header():
    client = app.test_client()
    rsp = client.post('/edit_recipe/1')
    assert rsp.status == '500 INTERNAL SERVER ERROR'

def test_delete_recipe_page_header():
    client = app.test_client()
    rsp = client.post('/delete_recipe/1')
    assert rsp.status == '500 INTERNAL SERVER ERROR'
    
def test_logout_page_header():
    client = app.test_client()
    rsp = client.get('/logout')
    assert rsp.status == '500 INTERNAL SERVER ERROR'
