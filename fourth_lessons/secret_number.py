import random

random_number = random.randint(1, 10)

while True:
    try:
        input_number = int(input('Please input your number: '))
        if input_number == 0:
            print('Game over!')
            break
        elif input_number == random_number:
            print('Congratulation!')
        else:
            continue
    except ValueError:
        print('Invalid input')
