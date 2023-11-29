# Modify your program again so that the chosen password cannot be one of a list of
# common passwords, defined thus:

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

entered_password = input("Enter your password: ")

if len(entered_password) >= 8 and len(entered_password) <= 12:
    if entered_password in BAD_PASSWORDS:
        print("Password is too common")
    else:
        print("Password saved successfully!")
else:
    print("Password length is too short")
