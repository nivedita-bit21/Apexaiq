import pytest
import requests  # Import requests module to handle exceptions
from api_client import APIClient

# Constants
BASE_URL = "https://jsonplaceholder.typicode.com"
POST_ID = 1


@pytest.fixture
def api_client():
    """Fixture to create an APIClient instance."""
    return APIClient(BASE_URL)


def test_get_posts(api_client):
    """Test if the posts API returns a valid response."""
    response_data = api_client.get_posts()

    # Assertions
    assert isinstance(response_data, list), "Expected a list of posts"
    assert len(response_data) > 0, "Expected at least one post"
    assert "id" in response_data[0], "Each post should have an 'id' field"


def test_get_post_by_id(api_client):
    """Test if the API returns a post by ID."""
    response_data = api_client.get_post_by_id(POST_ID)

    # Assertions
    assert "id" in response_data, "Response should have an 'id' field"
    assert response_data["id"] == POST_ID, f"Expected post ID {POST_ID}, got {response_data['id']}"


def test_invalid_post_id(api_client):
    """Test API response for a non-existing post ID."""
    with pytest.raises(requests.exceptions.HTTPError):  # This now works correctly
        api_client.get_post_by_id(9999)  # Invalid post ID that doesn't exist


if __name__ == "__main__":
    pytest.main(["-v"])
