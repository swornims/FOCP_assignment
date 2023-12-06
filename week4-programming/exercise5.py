# Write and test a function that converts a temperature measured in degrees
# centigrade into the equivalent in fahrenheit, and another that does the reverse
# conversion. Test both functions. (Google will find you the formulae).

def to_celsius(temp):
    """Converts the entered temperature in Fahrenheit to Celsius"""
    conv_temp = (temp - 32) * 5/9
    return print(f"Temperature in Celsius: {conv_temp}")


def to_fahrenheit(temp):
    """Converts the entered temperature in Celsius to Fahrenheit"""
    conv_temp = temp * 9/5 + 32
    return print(f"Temperature in Fahrenheit: {conv_temp}")


entered_temp = float(input('Enter your temperature: '))

to_celsius(entered_temp)
to_fahrenheit(entered_temp)
