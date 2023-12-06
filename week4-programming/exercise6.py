# Write a program that takes a centigrade temperature and displays the equivalent in
# fahrenheit. The input should be a number followed by a letter C. The output should
# be in the same format.

def to_fahrenheit(temp):
    """Converts the entered temperature in Celsius to Fahrenheit"""
    conv_temp = float(temp[:-1])
    return print(f"{temp} converted to Fahrenheit is: {conv_temp * 9/5 + 32}F")


entered_temp = input("Enter your temperature: ")

to_fahrenheit(entered_temp)
