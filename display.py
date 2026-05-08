def print_banner():
    print("""
╔══════════════════════════════════════════════╗
║        REST CLIENT  —  JSONPlaceholder       ║
║   GET · POST · PUT · DELETE  in Python       ║
╚══════════════════════════════════════════════╝
    """)


def print_menu():
    print("""
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
  └─────────────────────────────────────┘""")


def divider(title=""):
    width = 50
    print(f"\n{'─' * width}")
    if title:
        print(f"  {title}")
        print(f"{'─' * width}")


def print_post(post):
    """Display a single post in a readable format."""
    print(f"""
  ┌─ Post Details {'─' * 34}
  │  ID      : {post.get('id', 'N/A')}
  │  User ID : {post.get('userId', 'N/A')}
  │  Title   : {post.get('title', 'N/A')}
  │
  │  Body:
  │  {_wrap_text(post.get('body', ''), width=60, indent='  │  ')}
  └{'─' * 49}""")


def print_posts_table(posts):
    """Display a list of posts as a simple table."""
    print(f"  {'ID':<5} {'User':<6} {'Title'}")
    print(f"  {'─'*4} {'─'*5} {'─'*40}")
    for post in posts:
        title = post.get('title', '')[:42]
        print(f"  {post.get('id', ''):<5} {post.get('userId', ''):<6} {title}")


def print_comment(comment):
    """Display a single comment."""
    print(f"  ▸ [{comment.get('id')}] {comment.get('name', '')[:50]}")
    print(f"    Email : {comment.get('email', '')}")
    print(f"    Body  : {comment.get('body', '')[:70]}...")
    print()


def print_success(message):
    print(f"\n  ✓  {message}")


def print_error(message):
    print(f"\n  ✗  Error: {message}")


# ──────────────────────────────────────────
# PRIVATE HELPER
# ──────────────────────────────────────────
def _wrap_text(text, width=60, indent=""):
    """
    Break a long string into lines of max `width` characters.
    Used to display long post bodies inside the box.
    """
    words   = text.split()
    lines   = []
    current = ""

    for word in words:
        # If adding the next word fits in the width, add it
        if len(current) + len(word) + 1 <= width:
            current += (" " if current else "") + word
        else:
            # Otherwise start a new line
            lines.append(current)
            current = word

    if current:
        lines.append(current)

    # Join lines together with the indent for the box border
    return f"\n{indent}".join(lines)
