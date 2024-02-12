def key_in_dictionary(dict1, dict2):
    new_dict = {}

    for key, value in dict1.items():
        new_dict[key] = value

    for key, value in dict2.items():
        if key in new_dict:
            new_dict[key] += value
        else:
            new_dict[key] = value

    return new_dict


print(key_in_dictionary({'a': 3, 'sa': 21, 'er': 4}, {'ef': 31, 'sa': 3, 'er': 54}))
