a = int(input('Please enter first number: '))
b = int(input('Please enter second number: '))
c = int(input('Please enter third number: '))

if a < b and a < c:
    print(f'Minimum number is: {a}')
elif b < a and b < c:
    print(f'Minimum number is: {b}')
else:
    print(f'Minimum number is: {c}')
