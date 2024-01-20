import hashlib


def add_user(file, new_username, new_fullname, hashed_password):
    """Adds the verified credentials of an user to the passwd.txt file."""

    file.write(f"\n{new_username}:{new_fullname}:{hashed_password}")
    print("User added successfully!")


def password_hash(new_password):
    """Hashes the entered password in the SHA256 Format."""

    hasher = hashlib.sha256()
    hasher.update(new_password.encode())
    return hasher.hexdigest()


def username_validation(file, new_username, new_fullname, new_password):
    """Checks whether the entered username already exists in the passwd.txt file."""

    username_list = []
    for line in file:
        username_list.append(line.split(":")[0])

    if new_username in username_list:
        raise ValueError("Cannot add. Most likely username already exists.")
    else:
        hashed_password = password_hash(new_password)
        add_user(file, new_username, new_fullname, hashed_password)


if __name__ == '__main__':
    """Validates the input and passes it to other functions for processing."""

    with open("passwd.txt", "r+") as file:

        new_username = str(input("Enter new username: "))

        while len(new_username.strip(" ")) <= 0:
            print("No username recorded! Try again.")
            new_username = str(input("Username to delete: "))
        else:
            new_username

        new_fullname = str(input("Enter full name: "))

        while len(new_fullname.strip(" ")) <= 0:
            print("No username recorded! Try again.")
            new_fullname = str(input("Enter full name: "))
        else:
            new_fullname

        new_password = str(input("Enter password: "))

        while len(new_password.strip(" ")) <= 0:
            print("No username recorded! Try again.")
            new_password = str(input("Enter full name: "))
        else:
            new_password

        try:
            username_validation(file, new_username, new_fullname, new_password)
        except ValueError as e:
            print(e)
