def unique_line(first_file, second_file):
    list1 = []
    list2 = []

    with open(first_file, 'r') as file1:
        for line in file1:
            list1.append(line.strip())

    with open(second_file, 'r') as file2:
        for line in file2:
            list2.append(line.strip())

    return [i for i in list1 if i not in list2]



print(unique_line('my_file.txt', 'new_file.txt'))