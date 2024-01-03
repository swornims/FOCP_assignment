# Last week you wrote a program that processed a collection of temperature readings
# entered by the user and displayed the maximum, minimum, and mean. Create a
# version of that program that takes the values from the command-line instead. Be
# sure to handle the case where no arguments are provided!

import sys
from statistics import mean

args = sys.argv[1:]


if len(args) == 0:
    print("No temperatures entered!")
else:
    temperatues = list(map(float, args))
    max_temp = max(temperatues)
    min_temp = min(temperatues)
    mean_temp = mean(temperatues)

    print(f"The max temperature is: {max_temp},\nThe min temperature is: {
        min_temp},\nThe mean temperature is: {mean_temp}")
