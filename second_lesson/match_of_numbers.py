a = int(input('Please enter first number: '))
b = int(input('Please enter second number: '))
c = int(input('Please enter third number: '))

if a == b == c:
    print('3')
elif a == b or b == c or a == c:
    print('2')
else:
    print('0')