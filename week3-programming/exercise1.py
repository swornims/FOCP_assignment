number = int(input('Enter a number: '))

for i in range(1, 13):
    print(f"{number} x {i} = {i*number}")


password = input("Enter a password: ")
special = "#$%&@"
up_valid = lw_valid = special_valid = num_valid = False

if 8 <= len(password) <= 16:
    for char in password:
        if char.isupper():
            up_valid = True

        if char.islower():
            lw_valid = True

        if char.isdigit():
            num_valid = True

        if char in special:
            special_valid = True

print("Valid password") if (up_valid and lw_valid and special_valid and num_valid) else print(
    "Invalid password, try again")
