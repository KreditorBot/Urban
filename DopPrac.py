grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()
#stud_s = sorted(students)

grades_m = []
for num in grades:
        s = sum(num)/len(num)
        grades_m.append(s)

dictionary = dict(zip(students, grades_m))
print(dictionary)