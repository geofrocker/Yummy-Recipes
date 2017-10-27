"""Test for yummy recipe web app"""
from app import app

def test_home_page_header():
    """Test home page"""
    client = app.test_client()
    rsp = client.get('/')
    import pdb; pdb.set_trace()
    assert rsp.status == '200 OK'

def test_login_page_header():
    """Test login_page"""
    client = app.test_client()
    rsp = client.get('/login')
    assert rsp.status == '200 OK'

def test_register_page_header():
    """Test register_page"""
    client = app.test_client()
    rsp = client.get('/register')
    assert rsp.status == '200 OK'

def test_dashboard_page_header():
    """Test dashboard_page"""
    client = app.test_client()
    rsp = client.get('/dashboard')
    assert rsp.status == '200 OK'

def test_add_recipe_page_header():
    """Test edit_recipe_page"""
    client = app.test_client()
    rsp = client.post('/add_recipe')
    assert rsp.status == '200 OK'

def test_edit_recipe_page_header():
    """Test edit_recipe_page"""
    client = app.test_client()
    rsp = client.post('/edit_recipe/1')
    assert rsp.status == '302 FOUND'

def test_delete_recipe_page_header():
    """Test delete_recipe_page"""
    client = app.test_client()
    rsp = client.post('/delete_recipe/1')
    assert rsp.status == '302 FOUND'

def test_logout_page_header():
    """Test logout_page"""
    client = app.test_client()
    rsp = client.get('/logout')
    assert rsp.status == '302 FOUND'
