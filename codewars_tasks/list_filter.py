def filter_list(l):
    return [i for i in l if not isinstance(i, str)]


print(filter_list([1,'a','b',0,15]))