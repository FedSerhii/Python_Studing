def pair_numbers(my_list):
    pair_numbers_list = []
    for i in my_list:
        if my_list.count(i) == 2:
            pair_numbers_list.append(i)
    return list(set(pair_numbers_list))


print(pair_numbers([2, 43, 21, 3, 2, 43, 65]))

# переписать с повторяющими символами
# прочесть функцию map
# написать функцию фильтр(func, iterable_obj):
# return новый список только из тех элементов котрые True