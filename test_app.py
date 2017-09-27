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
    