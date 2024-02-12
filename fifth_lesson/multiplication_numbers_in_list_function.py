def multiplication(a):
    return a * 2


def my_map(func, iterable_obj):
    tuple_of_result = []
    for i in iterable_obj:
        tuple_of_result.append(func(i))

    result = set(tuple_of_result)
    result = list(result)

    result.sort()

    return result

print(my_map(multiplication, [2, 3, 3, 5, 3, 5]))

# def numbers_multiplication(my_list):
#     new_list = []
#
# #     for i in my_list:
# #         new_list.append(i * 2)
# #
# #     return new_list
# #
# #
# # print(numbers_multiplication([2, 35, 3, 5, 55]))
