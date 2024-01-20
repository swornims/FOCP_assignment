import getpass
import hashlib


def read_file():
    """Reads the passwd.txt file and returns the data stored in lists."""

    content_list = []
    username_list = []
    password_list = []
    with open("passwd.txt", "r") as file:
        for line in file:
            content_list.append(line)
            username_list.append(line.strip().split(":")[0])
            password_list.append(line.strip().split(":")[2])

    return content_list, username_list, password_list


def rewrite_file(content_list):
    """Rewrites the content file after it removes empty lines from it."""

    stripped_list = [line.rstrip() for line in content_list if line.strip()]

    with open("passwd.txt", "w") as file:
        file.write('\n'.join(stripped_list))


def password_hash(entered_password):
    """Hashes the entered password in the SHA256 Format."""

    hasher = hashlib.sha256()
    hasher.update(entered_password.encode())

    return hasher.hexdigest()


def del_user(entered_username, entered_password):
    """Deletes the user if all the validations are successful."""

    content, username, password = read_file()

    if (entered_username not in username or password_hash(entered_password) != password[username.index(entered_username)]):
        raise ValueError("Credential Error!")
    else:
        content.pop(username.index(entered_username))
        print(f"Username {entered_username} deleted successfully!")
        rewrite_file(content)


if __name__ == '__main__':
    """Validates the input and passes it to other functions for processing."""

    entered_username = str(input("Username to delete: "))

    while len(entered_username.strip(" ")) <= 0:
        print("No username recorded! Try again.")
        entered_username = str(input("Username to delete: "))
    else:
        entered_username

    entered_password = getpass.getpass(prompt="Password: ")

    while len(entered_password.strip(" ")) <= 0:
        print("No password entered! Try again.")
        entered_password = getpass.getpass(prompt="Password: ")
    else:
        entered_password

    try:
        del_user(entered_username, entered_password)
    except ValueError as e:
        print(e)
