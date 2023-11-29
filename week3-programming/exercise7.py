# Modify your "Times Table" program so that the user enters the number of the table
# they require. This number should be between 0 and 12 inclusive.


entered_num = int(input("Enter a number: "))

if entered_num in range(0, 13):
    for i in range(0, 13):
        print(f"{i} x {entered_num} = {i*entered_num}")
else:
    print("Enter a number between range 0-12")
