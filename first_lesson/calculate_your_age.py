from datetime import datetime

try:
    name = input('Please input your name: ')
    birth_year = int(input('Please input your birth year: '))
    birth_month = int(input('Please input your birth month: '))
    birth_day = int(input('Please input your birthday: '))

    birth_date = datetime(birth_year, birth_month, birth_day)

    current = datetime.today()

    age = current.year - birth_date.year
    if (current.month, current.day) <= (birth_date.month, birth_date.day):
        age -= 1
    print(f'{name}, your age is {age}')
except ValueError as i:
    print(f'Invalid input!\n'
          f'Error: {i}')