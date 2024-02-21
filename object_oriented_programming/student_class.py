class Student:
    def __init__(self, name, surname, grade_list):
        self.name = name
        self.surname = surname
        self.grade_list = grade_list

    def __len__(self):
        return len(self.grade_list)

stud1 = Student('Serhii', 'Fed', [75, 80, 87, 93])
stud2 = Student('Alex', 'Kush', [79, 95, 64])
stud3 = Student('Evhen', 'Gerb', [85, 67, 74, 92, 69])

students = [stud1, stud2, stud3]

students_sort = sorted(students, key=lambda x: len(x), reverse=True)

for students in students_sort:
    print(f'{students.surname} {students.name} have: {students.grade_list} grades')