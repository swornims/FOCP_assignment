# Write a program that reads 6 temperatures (in the same format as before), and
# displays the maximum, minimum, and mean of the values.
# Hint: You should know there are built-in functions for max and min. If you hunt, you
# might also find one for the mean.

from statistics import mean


def read_temperatures():
    """
    Reads 6 temperatures from the user, calculates and displays the maximum, minimum,
    and mean of these temperatures.
    """
    temperatures = []
    for i in range(6):
        temp = float(input(f"Enter temperature {i+1}: "))
        temperatures.append(temp)

    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = mean(temperatures)

    return max_temp, min_temp, mean_temp


max_temp, min_temp, mean_temp = read_temperatures()


print(f"The max temperature is: {max_temp},\nThe min temperature is: {
      min_temp},\nThe mean temperature is: {mean_temp}")
