import requests
import pytest

@pytest.fixture(scope="session")
def base_url():
    return "https://reqres.in/api"

def test_list_users(base_url):
    url = f"{base_url}/users"
    response = requests.get(url)
    assert response.status_code == 200
    assert "data" in response.json()

def test_single_user(base_url):
    url = f"{base_url}/users/2"
    response = requests.get(url)
    assert response.status_code == 200
    # assert "data" in response.json()

def test_single_user_not_found(base_url):
    url = f"{base_url}/users/999"
    response = requests.get(url)
    assert response.status_code == 404
#     assert response.json()["error"] == "User not found."

def test_list_resource(base_url):
    resource = "products"
    url = f"{base_url}/{resource}"
    response = requests.get(url)
    assert response.status_code == 200
    assert "data" in response.json()

def test_single_resource(base_url):
    resource = "products"
    resource_id = 3
    url = f"{base_url}/{resource}/{resource_id}"
    response = requests.get(url)
    assert response.status_code == 200
    assert "data" in response.json()

def test_single_resource_not_found(base_url):
    resource = "products"
    resource_id = 999
    url = f"{base_url}/{resource}/{resource_id}"
    response = requests.get(url)
    assert response.status_code == 404
    # assert "error" in response.json()

def test_create_resource(base_url):
    resource = "users"
    url = f"{base_url}/{resource}"
    payload = {
        "name": "John Doe",
        "job": "Developer"
    }
    response = requests.post(url, data=payload)
    assert response.status_code == 201
    assert "id" in response.json()

def test_update_resource(base_url):
    resource = "users"
    resource_id = 2
    url = f"{base_url}/{resource}/{resource_id}"
    payload = {
        "name": "Jane Smith",
        "job": "Designer"
    }
    response = requests.put(url, data=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Smith"
    assert response.json()["job"] == "Designer"

def test_delete_resource(base_url):
    resource = "users"
    resource_id = 2
    url = f"{base_url}/{resource}/{resource_id}"
    response = requests.delete(url)
    assert response.status_code == 204

def test_successful_registration():
    url = "https://reqres.in/api/register"
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    response = requests.post(url, data=payload)
    assert response.status_code == 200  # Corrected status code assertion

def test_unsuccessful_registration(base_url):
    url = f"{base_url}/register"
    payload = {
        "email": "test@example.com"
    }
    response = requests.post(url, data=payload)
    assert response.status_code == 400
    assert "error" in response.json()

def test_successful_login(base_url):
    url = f"{base_url}/login"
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = requests.post(url, data=payload)
    assert response.status_code == 200
    assert "token" in response.json()

def test_unsuccessful_login(base_url):
    url = f"{base_url}/login"
    payload = {
        "email": "test@example.com",
        "password": "incorrect"
    }
    response = requests.post(url, data=payload)
    assert response.status_code == 400
    assert "error" in response.json()

def test_delayed_response(base_url):
    url = f"{base_url}/users?delay=3"
    response = requests.get(url)
    assert response.status_code == 200
    assert "data" in response.json()