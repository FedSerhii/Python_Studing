def order(sentence):
    new_list = sentence.split()
    some_list = []
    some_list_1 = []
    number_string = '1 2 3 4 5 6 7 8 9'
    number_string = number_string.split()
    for i in new_list:
        for char in number_string:
            if char in i:
                some_list.append(char + i)
    some_list.sort()
    for i in some_list:
        some_list_1.append(i[1:])
    return ' '.join(some_list_1)