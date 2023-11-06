# Exercise 5

# def sum(arr):
#     if len(arr) == 1:
#         return arr[0]
#     else:
#         return arr[0] + sum(arr[1:])


class_size = [113, 175, 12]
lab_group = 24

for student in class_size:
    complete_groups = student // lab_group
    remaining_students = student % lab_group

    print('Group size:', student)
    print('Total number of complete groups:', complete_groups)
    print('Remaining students:', remaining_students)


# total_students = sum(arr)
# complete_groups, remaining_students = divmod(total_students, lab_group)
