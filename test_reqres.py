import requests
import pytest
 
BASE_URL = "https://jsonplaceholder.typicode.com"
 
@pytest.fixture
def base_url():
    """It returns the base url."""
    return BASE_URL
 
def test_get_all_posts(base_url):
    """ It retrives the all post."""
    response = requests.get(f"{base_url}/posts", timeout=10)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0