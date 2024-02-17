c1 = int(input('Please enter the number of students in first class: '))
c2 = int(input('Please enter the number of students in the second class: '))
c3 = int(input('Please enter the number of students in the third class: '))

print(f'You should buy {c1 // 2 + c2 // 2 + c3 // 2 + c1 % 2 + c2 % 2 + c3 % 2} desks')