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
