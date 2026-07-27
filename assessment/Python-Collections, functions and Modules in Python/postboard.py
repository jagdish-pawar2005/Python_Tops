# PostBoard Application

users = {}
posts = []


# ------------------ User Functions ------------------

def register():
    print("\n=== Register ===")

    username = input("Enter username: ").strip()

    if username == "":
        print("Username cannot be empty!")
        return

    if username in users:
        print("Username already exists!")
        return

    password = input("Enter password: ").strip()

    if password == "":
        print("Password cannot be empty!")
        return

    users[username] = password
    print("Registration successful!")


def login():
    print("\n=== Login ===")

    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username in users and users[username] == password:
        print("Login successful!")
        return username

    print("Invalid username or password!")
    return None


# ------------------ Post Functions ------------------

def create_post(username):
    print("\n=== Create Post ===")

    title = input("Enter title: ").strip()

    if title == "":
        print("Title cannot be empty!")
        return

    description = input("Enter description: ").strip()

    if description == "":
        print("Description cannot be empty!")
        return

    date = input("Enter date (DD-MM-YYYY): ").strip()

    if date == "":
        print("Date cannot be empty!")
        return

    post = {
        "author": username,
        "title": title,
        "description": description,
        "date": date
    }

    posts.append(post)
    print("Post created successfully!")


def view_posts():
    print("\n=== All Posts ===")

    if not posts:
        print("No posts available.")
        return

    for i, post in enumerate(posts, start=1):
        print("\n---------------------------")
        print(f"Post #{i}")
        print(f"Author      : {post['author']}")
        print(f"Title       : {post['title']}")
        print(f"Date        : {post['date']}")
        print(f"Description : {post['description']}")
        print("---------------------------")


def search_posts():
    print("\n=== Search Posts By Username ===")

    username = input("Enter username: ").strip()

    found = False

    for post in posts:
        if post["author"].lower() == username.lower():
            found = True
            print("\n---------------------------")
            print(f"Author      : {post['author']}")
            print(f"Title       : {post['title']}")
            print(f"Date        : {post['date']}")
            print(f"Description : {post['description']}")
            print("---------------------------")

    if not found:
        print("No posts found for this user.")


# ------------------ User Menu ------------------

def user_menu(username):
    while True:
        print("\n===== PostBoard =====")
        print("1. Create Post")
        print("2. View All Posts")
        print("3. Search Posts By Username")
        print("4. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            create_post(username)

        elif choice == "2":
            view_posts()

        elif choice == "3":
            search_posts()

        elif choice == "4":
            print("Logged out successfully.")
            break

        else:
            print("Invalid choice!")


# ------------------ Main Program ------------------

while True:
    print("\n===== Welcome to PostBoard =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        user = login()

        if user:
            user_menu(user)

    elif choice == "3":
        print("Thank you for using PostBoard!")
        break

    else:
        print("Invalid choice!")