import requests
from display import print_post, print_posts_table, print_comment, print_success, print_error

BASE_URL = "https://jsonplaceholder.typicode.com"


class PostClient:
    """
    A simple REST client for the /posts and /comments endpoints
    of the JSONPlaceholder API.

    Attributes:
        base_url (str): The root URL for all API requests.
        session  (requests.Session): A reusable HTTP session
                 (faster than creating a new connection every request).
    """

    def __init__(self):
        self.base_url = BASE_URL
        # Session reuses the TCP connection — more efficient than requests.get() each time
        self.session  = requests.Session()

    # ──────────────────────────────────────────
    # PRIVATE HELPER
    # ──────────────────────────────────────────
    def _get(self, endpoint, params=None):
        """
        Internal helper: sends a GET request and returns parsed JSON.
        Returns None if something goes wrong.

        Args:
            endpoint (str): e.g. "/posts" or "/posts/1"
            params   (dict): optional query parameters e.g. {"userId": 2}
        """
        url = f"{self.base_url}{endpoint}"
        try:
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()      # raises HTTPError if status >= 400
            return response.json()
        except requests.exceptions.ConnectionError:
            print_error("No internet connection. Please check your network.")
        except requests.exceptions.Timeout:
            print_error("Request timed out. The server took too long to respond.")
        except requests.exceptions.HTTPError as e:
            print_error(f"HTTP error: {e.response.status_code} — {e.response.reason}")
        except requests.exceptions.RequestException as e:
            print_error(f"Unexpected error: {e}")
        return None

    # ──────────────────────────────────────────
    # 1. GET  —  All posts
    # ──────────────────────────────────────────
    def get_all_posts(self, limit=5):
        """
        Fetch all posts and display the first `limit` of them.

        Args:
            limit (int): How many posts to display (default 5).
        """
        data = self._get("/posts")
        if data is None:
            return

        print(f"\n  Total posts on server : {len(data)}")
        print(f"  Showing first {limit}:\n")
        print_posts_table(data[:limit])

    # ──────────────────────────────────────────
    # 2. GET  —  Single post by ID
    # ──────────────────────────────────────────
    def get_post(self, post_id):
        """
        Fetch and display a single post.

        Args:
            post_id (int): The ID of the post to retrieve.
        """
        data = self._get(f"/posts/{post_id}")
        if data:
            print_post(data)

    # ──────────────────────────────────────────
    # 3. GET  —  Posts filtered by user ID
    # ──────────────────────────────────────────
    def get_posts_by_user(self, user_id):
        """
        Fetch all posts written by a specific user.
        Uses a query parameter: /posts?userId=<user_id>

        Args:
            user_id (int): The user whose posts to retrieve.
        """
        data = self._get("/posts", params={"userId": user_id})
        if data is None:
            return

        print(f"\n  User #{user_id} has {len(data)} post(s):\n")
        print_posts_table(data)

    # ──────────────────────────────────────────
    # 4. GET  —  Comments on a post
    # ──────────────────────────────────────────
    def get_comments(self, post_id):
        """
        Fetch all comments for a given post.
        Endpoint: /posts/<post_id>/comments

        Args:
            post_id (int): The post whose comments to fetch.
        """
        data = self._get(f"/posts/{post_id}/comments")
        if data is None:
            return

        print(f"\n  Post #{post_id} has {len(data)} comment(s):\n")
        for comment in data:
            print_comment(comment)

    # ──────────────────────────────────────────
    # 5. POST  —  Create a new post
    # ──────────────────────────────────────────
    def create_post(self, title, body, user_id=1):
        """
        Send a POST request to create a new post.
        The server returns the new post with an assigned ID.

        Args:
            title   (str): Title of the post.
            body    (str): Body/content of the post.
            user_id (int): The author's user ID (default 1).
        """
        url = f"{self.base_url}/posts"

        payload = {
            "userId": user_id,
            "title":  title,
            "body":   body,
        }

        try:
            response = self.session.post(url, json=payload, timeout=10)
            response.raise_for_status()
            created = response.json()
            print_success(f"Post created! Server assigned ID: {created['id']}")
            print_post(created)
        except requests.exceptions.RequestException as e:
            print_error(f"Could not create post: {e}")

    # ──────────────────────────────────────────
    # 6. PUT  —  Update a post (full replace)
    # ──────────────────────────────────────────
    def update_post(self, post_id, title, body, user_id=1):
        """
        Send a PUT request to completely replace a post's data.
        Note: PUT replaces ALL fields — use PATCH if you only want
        to change one field (not covered here, but good to know!).

        Args:
            post_id (int): The ID of the post to update.
            title   (str): New title.
            body    (str): New body.
            user_id (int): Author user ID.
        """
        url = f"{self.base_url}/posts/{post_id}"

        payload = {
            "id":     post_id,
            "userId": user_id,
            "title":  title,
            "body":   body,
        }

        try:
            response = self.session.put(url, json=payload, timeout=10)
            response.raise_for_status()
            updated = response.json()
            print_success(f"Post #{post_id} updated successfully!")
            print_post(updated)
        except requests.exceptions.RequestException as e:
            print_error(f"Could not update post: {e}")

    # ──────────────────────────────────────────
    # 7. DELETE  —  Remove a post
    # ──────────────────────────────────────────
    def delete_post(self, post_id):
        """
        Send a DELETE request to remove a post.
        JSONPlaceholder always returns {} (empty dict) on success.

        Args:
            post_id (int): The ID of the post to delete.
        """
        url = f"{self.base_url}/posts/{post_id}"

        try:
            response = self.session.delete(url, timeout=10)
            response.raise_for_status()
            print_success(f"Post #{post_id} deleted. Server response: {response.json()}")
        except requests.exceptions.RequestException as e:
            print_error(f"Could not delete post: {e}")
