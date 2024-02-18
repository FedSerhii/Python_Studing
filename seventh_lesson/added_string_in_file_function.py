def added_string(path_file, string=''):
    string = input('Please input your string: ')
    file = open(path_file, 'w')
    file.write(string)
    file.close()


added_string('new_file.txt')


# def added_string():
#     my_string = input('Please input your string: ')
#     with open('my_file.txt', 'w') as file:
#         file.write(my_string)
#
#
# added_string()