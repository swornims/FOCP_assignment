# Functions are often used to validate input. Write a function that accepts a single
# integer as a parameter and returns True if the integer is in the range 0 to 100
# (inclusive), or False otherwise. Write a short program to test the function.

def int_checker(a):
    """This function takes in an integer as a parameter and returns True if the parameter is in the given range and returns False if it is not."""

    if a in range(0, 101):
        return print(True)
    else:
        return print(False)


entered_number = int(input("Enter a number: "))

int_checker(entered_number)
