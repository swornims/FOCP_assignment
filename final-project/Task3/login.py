import getpass
import hashlib


def password_hash(entered_password):
    """Hashes the entered password in the SHA256 Format."""

    hasher = hashlib.sha256()
    hasher.update(entered_password.encode())
    return hasher.hexdigest()


def login_user(entered_username, entered_password):
    """Checks all the validation fields and logs in the user."""

    username_list = []
    password_list = []
    with open("passwd.txt", "r") as file:
        for line in file:
            username = line.strip().split(":")[0]
            password = line.strip().split(":")[2]
            username_list.append(username)
            password_list.append(password)

    if (entered_username not in username or password_hash(entered_password) != password_list[username_list.index(entered_username)]):
        raise ValueError("Credential Error!")
    else:
        print(f"Logged in as {entered_username}")


if __name__ == '__main__':
    """Validates the input and passes it to other functions for processing."""

    entered_username = str(input("Enter your username: "))

    while len(entered_username.strip(" ")) <= 0:
        print("No username recorded! Try again.")
        entered_username = str(input("Enter your username: "))
    else:
        entered_username

    entered_password = getpass.getpass(prompt="Enter your password: ")

    while len(entered_password.strip(" ")) <= 0:
        print("No password entered! Try again.")
        entered_password = getpass.getpass(prompt="Enter your password: ")
    else:
        entered_password

    try:
        login_user(entered_username, entered_password)
    except ValueError as e:
        print(e)
