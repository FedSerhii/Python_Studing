class Student:

    total_student = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.total_student += 1

    @classmethod
    def info_total_student(cls):
        print(f'Total student is: {cls.total_student}')

stud1 = Student('Serhii', 29)
stud2 = Student('Evhen', 24)
stud3 = Student('Alex', 25)
stud4 = Student('Artur', 21)

Student.info_total_student()