def find_uniq(arr):
    new_dict = {}

    for i in arr:
        if i in new_dict:
            new_dict[i] += 1
        else:
            new_dict[i] = 1

    n = next(key for key, value in new_dict.items() if value == 1)

    return n


print(find_uniq([ 0, 0, 0.55, 0, 0 ]))