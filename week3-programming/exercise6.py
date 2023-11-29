# Write a program that displays the "Seven Times Table". That is, the result of
# multiplying 7 by every number from 0 to 12 inclusive.

entered_num = int(input("Enter a number: "))

for i in range(0, 13):
    print(f"{i} x {entered_num} = {i*entered_num}")
