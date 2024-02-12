def factorial_of_number(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial_of_number(5))
