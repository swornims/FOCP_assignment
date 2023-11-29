# Modify your greeting program so that if the user does not enter a name (i.e. they
# just press enter), the program responds "Hello, Stranger!". Otherwise it should print
# a greeting with their name as before.

entered_name = input("Enter your name: ")

if entered_name == '':
    print("Hello, Stranger!")
else:
    print(f"Hello, {entered_name}")
