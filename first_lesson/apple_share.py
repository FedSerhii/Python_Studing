n = int(input('Please enter the number of students: '))
k = int(input('Please enter the number of apples: '))

if n > 0 and k > 0:
    amount_apple_for_student = k // n
    amount_apple_in_box = k % n
    print(f'Amount apple for student is: {amount_apple_for_student}\n'
          f'Amount apple in box is: {amount_apple_in_box}')
elif n < 0 and k < 0:
    print('Incorrect input, please try again!')
elif k == 0:
    print('Nobody got any apples!')
else:
    print('Invalid input!')
