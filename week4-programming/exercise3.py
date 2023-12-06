# Modify your "greetings" program so that the first letter of the name entered is
# always in uppercase with the rest in lowercase. This should happen even if the user
# entered their name differently. So if the user entered arthur, ARTHUR, or even
# arTHur the name should be displayed as Arthur.

def case_manager(name):
    """This function takes in a string as a parameter and changes the first character to uppercase and the rest to lowercase."""

    return name[0].upper() + name[1:].lower()


entered_name = input('Hello, What is your name? ')

print(f"Hello, {case_manager(entered_name)}. Good to meet you!")
