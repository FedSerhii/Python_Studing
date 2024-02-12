def sort_array(source_array):
    numbers_sorted = sorted(i for i in source_array if i % 2 != 0)

    for key, value in enumerate(source_array):
        if value % 2 != 0:
            source_array[key] = numbers_sorted.pop(0)

    return source_array


print(sort_array([5, 3, 2, 8, 1, 4]))


# def sort_array(arr):
#   odds = sorted((x for x in arr if x%2 != 0), reverse=True)
#   return [x if x%2==0 else odds.pop() for x in arr]