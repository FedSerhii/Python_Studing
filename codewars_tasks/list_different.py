def array_diff(a, b):
    a = list(filter(lambda x: x not in b, a))
    return a
