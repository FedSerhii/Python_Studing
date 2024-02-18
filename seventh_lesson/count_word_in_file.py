def count_word(path_file):
    file = open(path_file, 'r')
    data = file.read()
    file.close()
    return len(data.split())


print(count_word('my_file.txt'))
# with open('my_file.txt', 'r') as file:
#     data = file.read()
#     print(len(data.split()))