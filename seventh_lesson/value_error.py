try:
    number1 = int(input('Please input first number: '))
    number2 = int(input('Please input second number: '))
    print(number1 + number2)
except ValueError:
    print('Input only numbers')
