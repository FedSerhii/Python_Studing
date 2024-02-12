def square_sum(numbers):
    numbers_list = []
    for i in numbers:
        numbers_list.append(i**i)

    return sum(numbers_list)


print(square_sum([1, 2, 2]))