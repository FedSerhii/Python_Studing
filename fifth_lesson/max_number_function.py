def max_number(list_of_numbers):
    max_numbers = list_of_numbers[0]
    for i in list_of_numbers:
        if i > max_numbers:
            max_numbers = i

    return max_numbers


print(max_number([1, 2, 4, 76, 3, 57]))
