def pair_of_symbols(my_string):
    if len(my_string) % 2 == 0:
        return True
    else:
        return False


my_list = ['asff', 'afreve', 'fgffgft']


def my_filter(func, iterable_obj):
    result = []

    for i in iterable_obj:
        if func(i) is True:
            result.append(i)

    return result

print(my_filter(pair_of_symbols, my_list))
