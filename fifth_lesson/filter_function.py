def filter_function(func, iterable_obj):
    result = []

    for i in iterable_obj:
        if func(i):
            result.append(i)

    return result


print(filter_function(lambda x: x % 2 == 0, [1, 3, 4, 6, 7, 8]))