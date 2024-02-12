def dict_string(my_string):
    result_dict = {}

    for i in my_string:
        if i in result_dict:
            result_dict[i] += 1
        else:
            result_dict[i] = 1

    return result_dict


print(dict_string('Hello Serhii'))
