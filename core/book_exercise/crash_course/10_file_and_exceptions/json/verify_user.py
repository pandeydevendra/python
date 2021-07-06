import json


def get_stored_username():
    """Get stored username if available."""
    try:
        filename = 'username.json'
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"""Username is {username}.""")
        verify_user = input("Is this the correct name?(y/n): ")
        if verify_user == 'y':
            print(f"""Welcome back {username}!""")
        elif verify_user == 'n':
            username = get_new_username()

    else:
        username = get_new_username()
        print(f"""We'll remember you when you come back {username}!""")

greet_user()