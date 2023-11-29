# Write a program that simulates the way in which a user might choose a password.
# The program should prompt for a new password, and then prompt again. If the two
# passwords entered are the same the program should say "Password Set" or
# similar, otherwise it should report an error.

password = input("Enter your password: ")
confirm_password = input("Confirm your password: ")

if password == confirm_password:
    print("Password Set")
else:
    print("Incorrect password")
