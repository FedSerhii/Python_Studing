my_number = int(input())

factorial = 1

for i in range(1, (my_number + 1)):
    factorial *= i

    print(f'Factorial of your number = {factorial}')