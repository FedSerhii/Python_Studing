total_sum = 0

while True:
    try:
        number = int(input())
        if number < 0:
            break
        total_sum += number
        print(total_sum)
    except ValueError:
        print('Invalid input!')

print(f'Your total sum = {total_sum}')
