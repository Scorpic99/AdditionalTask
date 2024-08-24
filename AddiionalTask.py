grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bildo', 'Steve', 'Khendrik', 'Aaron'}
a = 0
students_sort = sorted(students)
grades_list = []
while a < len(students):
    grades_list.append(sum(grades[a]) / len(grades[a]))
    a = a + 1
students_dict = dict(zip(students_sort, grades_list))
print(students_dict)