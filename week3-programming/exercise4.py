# Modify your program again so that the chosen password cannot be one of a list of
# common passwords, defined thus:

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']


password = input("Enter your password: ")
confirm_password = input("Confirm your password: ")
valid_password = valid_length = good_password = False

if len(password) >= 8 and len(password) <= 12:
    valid_length = True

    if password not in BAD_PASSWORDS:
        good_password = True

    if password == confirm_password:
        valid_password = True

print("Valid password") if valid_length and valid_password and good_password else print(
    "Invalid password. Enter again")
