file = open('my_file.txt', 'w')
file.write('My test file bla bla bla\n')
file.close()

try:
    file = open('any_file.txt', 'r')
    file_text = file.read()
    print(file_text)
    file.close()
except FileNotFoundError:
    print('File does not exist')
