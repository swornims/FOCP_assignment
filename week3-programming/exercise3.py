# Modify your previous program so that the password must be between 8 and 12
# characters (inclusive) long.

password = input("Enter your password: ")
confirm_password = input("Confirm your password: ")
valid_password = valid_length = False

if 8 <= len(password) >= 12:
    valid_length = True

    if password == confirm_password:
        valid_password = True

print("Valid password") if valid_length and valid_password else print(
    "Invalid password. Enter again")
