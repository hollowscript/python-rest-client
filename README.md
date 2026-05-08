# 🌐 REST Client — JSONPlaceholder API

A command-line Python project that demonstrates how to use the `requests` library to interact with a REST API using all four main HTTP methods: **GET, POST, PUT, and DELETE**.

Built with the [JSONPlaceholder](https://jsonplaceholder.typicode.com) free fake API — no account or API key needed.

---

## 📸 Preview

```
╔══════════════════════════════════════════════╗
║        REST CLIENT  —  JSONPlaceholder       ║
║   GET · POST · PUT · DELETE  in Python       ║
╚══════════════════════════════════════════════╝

  ┌─────────────────────────────────────┐
  │             MAIN MENU               │
  ├─────────────────────────────────────┤
  │  1  → Get all posts                 │
  │  2  → Get a single post             │
  │  3  → Get posts by user             │
  │  4  → Get comments on a post        │
  │  5  → Create a new post             │
  │  6  → Update a post                 │
  │  7  → Delete a post                 │
  │  0  → Exit                          │
  └─────────────────────────────────────┘
```

---

## 🚀 Features

- **GET** — Fetch all posts, a single post, posts by user, and comments
- **POST** — Create a new post with custom title and body
- **PUT** — Update an existing post completely
- **DELETE** — Delete a post with confirmation prompt
- Interactive menu-driven CLI — no arguments needed, just run and pick
- Clean error handling for connection errors, timeouts, and HTTP errors
- Uses `requests.Session()` for efficient, reusable connections

---

## 🛠️ Technologies Used

| Tool | Purpose |
|---|---|
| Python 3.x | Core language |
| `requests` | HTTP requests library |
| JSONPlaceholder | Free fake REST API for testing |

---

## 📁 Project Structure

```
rest_client/
│
├── main.py           # Entry point — runs the interactive menu
├── client.py         # PostClient class — all API/HTTP logic
├── display.py        # All print/formatting functions
├── requirements.txt  # Project dependencies
└── README.md         # This file
```

### Why three files?

This project uses a pattern called **Separation of Concerns**:

- `client.py` only handles HTTP logic — it doesn't know how to print anything
- `display.py` only handles how things look — it doesn't know about the API
- `main.py` connects them — it handles user input and calls the right functions

This makes the code easier to read, modify, and expand.

---

## ⚙️ Setup & Run

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

## 📖 What I Learned

- How to send HTTP requests using the `requests` library in Python
- The difference between GET, POST, PUT, and DELETE
- How to parse JSON responses into Python dicts and lists
- How to handle errors with `try/except` and `raise_for_status()`
- How to use query parameters (`?userId=2`) with `params=`
- How to use `requests.Session()` for connection reuse
- How to organize a Python project across multiple files

---

## 🔗 API Reference

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

> **Note:** JSONPlaceholder is a fake API. Data is not actually saved or deleted on the server — it only simulates those actions and returns realistic responses. This makes it perfect for learning.

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
