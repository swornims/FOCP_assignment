# Modify the previous program so that it can process any number of values. The input
# terminates when the user just pressed "Enter" at the prompt rather than entering a
# value

from statistics import mean


def read_temperatures():
    """
    Reads 6 temperatures from the user, calculates and displays the maximum, minimum,
    and mean of these temperatures.
    """
    temperatures = []
    i = 0
    end_input = False

    while end_input != True:
        entered_temp = input(f"Enter temperature {i+1}: ")
        i += 1

        if len(entered_temp) == 0:
            end_input = True
            break
        else:
            temp = float(entered_temp)
            temperatures.append(temp)

    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = mean(temperatures)

    return max_temp, min_temp, mean_temp


max_temp, min_temp, mean_temp = read_temperatures()


print(f"The max temperature is: {max_temp},\nThe min temperature is: {
      min_temp},\nThe mean temperature is: {mean_temp}")
