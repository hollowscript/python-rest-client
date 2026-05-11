## Features

- **GET** — Fetch all posts, a single post, posts by user, and comments
- **POST** — Create a new post with custom title and body
- **PUT** — Update an existing post completely
- **DELETE** — Delete a post with confirmation prompt
- Interactive menu-driven CLI — no arguments needed, just run and pick
- Clean error handling for connection errors, timeouts, and HTTP errors
- Uses `requests.Session()` for efficient, reusable connections

---

## Project Structure

```
rest_client/
│
├── main.py           # Entry point — runs the interactive menu
├── client.py         # PostClient class — all API/HTTP logic
├── display.py        # All print/formatting functions
├── requirements.txt  # Project dependencies
└── README.md         # This file
```

## API Reference

This project uses the [JSONPlaceholder API](https://jsonplaceholder.typicode.com).

**Note:** JSONPlaceholder is a fake API. Data is not actually saved or deleted on the server — it only simulates those actions and returns realistic responses.
