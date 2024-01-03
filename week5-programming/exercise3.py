# Write a program that takes a bunch of command-line arguments, and then prints
# out the shortest. If there is more than one of the shortest length, any will do.
# Hint: Don't overthink this. A good way to find the shortest is just to sort them.

import sys
args = sys.argv[1:]

print(sorted(list(map(float, args)))[0])
