def added_string():
    my_string = input('Please input your string: ')
    with open('my_file.txt', 'w') as file:
        file.write(my_string)


added_string()