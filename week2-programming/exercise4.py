# A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
# first count the sweets and then divide them according to how many pupils attend
# that day. Write a program that will tell the teacher how many sweets to give to each
# pupil, and how many she will have left over.

entered_no_of_sweets = int(input("Enter the number of sweets: "))
entered_no_of_students = int(
    input("Enter the total number of present students: "))

each_student = entered_no_of_sweets // entered_no_of_students
remaining_sweets = entered_no_of_sweets % entered_no_of_students

grammar = "sweets" if remaining_sweets != 1 else "sweets"

print(f"Each student will get {each_student} sweets and the teacher will have {
      remaining_sweets} {grammar} left over")
