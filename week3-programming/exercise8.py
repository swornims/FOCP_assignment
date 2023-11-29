entered_num = int(input("Enter a number: "))


if entered_num < 0:
    for i in range(12, 0, -1):
        print(f"{i} x {entered_num} = {i*entered_num}")
else:
    for i in range(0, 13):
        print(f"{i} x {entered_num} = {i*entered_num}")
