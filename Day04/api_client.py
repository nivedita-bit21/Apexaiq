import requests
import json


class APIClient:
    """A class to interact with the JSONPlaceholder API."""

    def __init__(self, base_url):
        """Initialize the APIClient with the base URL."""
        self.base_url = base_url

    def get_posts(self):
        """Fetch a list of posts and save them to a JSON file."""
        url = f"{self.base_url}/posts"
        response = requests.get(url)

        # Check for successful request
        response.raise_for_status()

        # Convert the response to JSON
        posts = response.json()

        # Save posts to a JSON file
        with open("posts.json", "w") as file:
            json.dump(posts, file, indent=4)

        return posts

    def get_post_by_id(self, post_id):
        """Fetch a single post by its ID."""
        url = f"{self.base_url}/posts/{post_id}"
        response = requests.get(url)

        # Check for successful request
        response.raise_for_status()
        return response.json()
