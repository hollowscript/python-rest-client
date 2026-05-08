# REST Client — JSONPlaceholder API

A command-line Python project that demonstrates how to use the `requests` library to interact with a REST API using all four main HTTP methods: **GET, POST, PUT, and DELETE**.

Built with the [JSONPlaceholder](https://jsonplaceholder.typicode.com) free fake API — no account or API key needed.


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

## Setup & Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/rest-client.git
cd rest-client
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the project

```bash
python main.py
```


---

## API Reference

This project uses the [JSONPlaceholder API](https://jsonplaceholder.typicode.com).

| Endpoint | Description |
|---|---|
| `GET /posts` | Fetch all posts |
| `GET /posts/{id}` | Fetch a single post |
| `GET /posts?userId={id}` | Filter posts by user |
| `GET /posts/{id}/comments` | Get comments for a post |
| `POST /posts` | Create a new post |
| `PUT /posts/{id}` | Update a post |
| `DELETE /posts/{id}` | Delete a post |

**Note:** JSONPlaceholder is a fake API. Data is not actually saved or deleted on the server — it only simulates those actions and returns realistic responses.
