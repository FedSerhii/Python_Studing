def copied_file(origin, copied):
    with open(origin, 'r') as file1:
        origin_text = file1.read()
        with open(copied, 'w') as file2:
            file2.write(origin_text)


copied_file('my_file.txt', 'new_file.txt')