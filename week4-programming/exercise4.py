# When processing data it is often useful to remove the last character from some
# input (it is often a newline). Write and test a function that takes a string parameter
# and returns it with the last character removed. (If the string contains one or fewer
# characters, return it unchanged.)

def char_remover(string):
    """This function takes in a string as a parameter and removes the last character of the string if its length is longer than 1."""

    if len(string) > 1:
        return print(f"String with the last letter removed: {string[:-1]}")
    else:
        return print("No changes")


entered_string = input("Enter a string: ")

char_remover(entered_string)
