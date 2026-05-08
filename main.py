from client import PostClient
from display import print_banner, print_menu, divider


def main():
    client = PostClient()
    print_banner()

    while True:
        print_menu()
        choice = input("  Enter your choice (0-7): ").strip()

        if choice == "1":
            divider("GET  ─  All Posts")
            limit = input("  How many posts to show? (press Enter for 5): ").strip()
            limit = int(limit) if limit.isdigit() else 5
            client.get_all_posts(limit=limit)

        elif choice == "2":
            divider("GET  ─  Single Post")
            post_id = input("  Enter post ID (1–100): ").strip()
            if post_id.isdigit():
                client.get_post(int(post_id))
            else:
                print("  ✗  Please enter a valid number.")

        elif choice == "3":
            divider("GET  ─  Posts by User")
            user_id = input("  Enter user ID (1–10): ").strip()
            if user_id.isdigit():
                client.get_posts_by_user(int(user_id))
            else:
                print("  ✗  Please enter a valid number.")

        elif choice == "4":
            divider("GET  ─  Comments on a Post")
            post_id = input("  Enter post ID to see its comments: ").strip()
            if post_id.isdigit():
                client.get_comments(int(post_id))
            else:
                print("  ✗  Please enter a valid number.")

        elif choice == "5":
            divider("POST  ─  Create New Post")
            title = input("  Title: ").strip()
            body  = input("  Body : ").strip()
            if title and body:
                client.create_post(title=title, body=body)
            else:
                print("  ✗  Title and body cannot be empty.")

        elif choice == "6":
            divider("PUT  ─  Update a Post")
            post_id = input("  Which post ID to update? (1–100): ").strip()
            if post_id.isdigit():
                title = input("  New title: ").strip()
                body  = input("  New body : ").strip()
                if title and body:
                    client.update_post(int(post_id), title=title, body=body)
                else:
                    print("  ✗  Title and body cannot be empty.")
            else:
                print("  ✗  Please enter a valid number.")

        elif choice == "7":
            divider("DELETE  ─  Delete a Post")
            post_id = input("  Which post ID to delete? (1–100): ").strip()
            if post_id.isdigit():
                confirm = input(f"  Are you sure you want to delete post #{post_id}? (y/n): ").strip().lower()
                if confirm == "y":
                    client.delete_post(int(post_id))
                else:
                    print("  Cancelled.")
            else:
                print("  ✗  Please enter a valid number.")

        elif choice == "0":
            print("\n  Goodbye! \n")
            break

        else:
            print("  ✗  Invalid choice. Please enter a number from 0 to 7.")

        input("\n  Press Enter to continue...")


if __name__ == "__main__":
    main()
