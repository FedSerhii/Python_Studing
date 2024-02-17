try:
    number1 = int(input('Please input first number: '))
    number2 = int(input('Please input second number: '))
    print(int(number1 / number2))
except ZeroDivisionError:
    print('Dividing by zero is not allowed')