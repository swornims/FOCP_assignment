# The Head of Computing at the University of Poppleton is tasked with dividing a
# group of students into lab groups. A lab group is usually 24 students, but this is
# sometimes varied to create groups of similar size. Write a program that prompts for
# the number of students and group size, and then displays how many groups will be
# needed and how many will be left over in a smaller group.
# How many students? 113
# Required group size? 22
# There will be 5 groups with 3 students left over.
# For bonus credit, see if you can fix the grammar in the output. So if there were 101
# students in groups of 20 the output would be:
# There will be 5 groups with 1 student left over.

entered_no_of_students = int(input("Enter the total number of students: "))
entered_lab_group = int(input("Enter the desired lab group size: "))

group_size = entered_no_of_students // entered_lab_group
remaining_students = entered_no_of_students % entered_lab_group

grammar = "students" if remaining_students != 1 else "student"

print(f"There will be {group_size} groups with {
      remaining_students} {grammar} left over")
