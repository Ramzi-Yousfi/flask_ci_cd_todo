from src import create_app

app = create_app()
from src.models.Todo import Todo


def test1():
    response = app.test_client().get('/')
    assert response.status_code == 200


def test2():
    response = app.test_client().get('/detail/1')
    assert response.status_code == 200


def test3():
    response = app.test_client().get('/detail/hello')
    assert response.status_code == 404


def test_update_todo():
    response = app.test_client().get('/update/1')
    todo = Todo('ramzi', 'helo', True)
    assert todo.title == 'ramzi'
    assert todo.description == 'helo'
    assert todo.done == True
    assert response.status_code == 200
    assert b"update" in response.data
    assert b"modifier" in response.data


def test_create():
    response = app.test_client().get('/create')
    todo = Todo('ramzi', 'devloppement',False)
    assert response.status_code == 200
    assert b"ajouter" in response.data
