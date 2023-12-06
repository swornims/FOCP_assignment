# Write a function that has a single string as its parameter, and returns the number of
# uppercase letters, and the number of lowercase letters in the string. Test the
# function with a short program.

def case_checker(entered_string):
    """This function takes in a string and counts the number of uppercase and lowercase letters in it."""
    for char in entered_string:
        print(char)


case_checker("AAAAsssss")
