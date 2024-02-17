try:
    value = int(input('Enter your number: '))
    print(f'Data type of {value} value', type(value))
except ValueError:
    print('Invalid input. Please enter a valid integer')


try:
    number1 = int(input('Enter your number1: '))
    number2 = int(input('Enter your number2: '))
    print(f'Sum: {number1 + number2}')
    print(f'Difference: {number1 - number2}')
    print(f'Product: {number1 * number2}')
    if number2 != 0:
        print(f'Quotient: {number1 / number2}')
    else:
        print('Cannot divide by zero')
except ValueError:
    print('Invalid input. Please enter a valid integer')