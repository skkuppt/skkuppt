from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}

def test_create_user_success():
    response = client.post(
        "/api/user/create",
        json={"username": "test3", "password1": "1234", "password2": "1234", "email": "test3@example.com"},
    )
    assert response.status_code == 204

    response = client.request("Delete",
        "/api/user/delete",
        json={"username": "test3", "password": "1234"},

    )
    assert response.status_code == 204
    

def test_create_user_fail():
    response = client.post(
        "/api/user/create",
        json={"username": "test4", "password1": "1234", "password2": "1234", "email": "test2@example.com"},
    )
    assert response.status_code == 409
    

def test_create_login_success():
    response = client.post(
        "/api/user/login",
        data={"username": "test", "password": "test", "grant_type": "password"},
        headers={"content-type": "application/x-www-form-urlencoded"}
    )
    
    assert response.status_code == 200
    response_data = response.json()
    assert "access_token" in response_data
    assert response_data["token_type"] == "bearer"
    assert "username" in response_data
    return response_data["token_type"], response_data["access_token"]

def test_create_login_fail():
    response = client.post(
        "/api/user/login",
        data={"username": "testfail", "password": "1234", "grant_type": "password"},
        headers={"content-type": "application/x-www-form-urlencoded"}
    )
    assert response.status_code == 401


def test_create_question():
    token_type, access_token = test_create_login_success()
    response = client.post(
        "/api/question/create",
        json={"topic": "test", "content": "test", "apikey": "test"},
        headers={"Authorization": f"{token_type} {access_token}"}
    )
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["answer"] == "test"