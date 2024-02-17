with open('my_file.txt', 'r') as file:
    data = file.read()
    print(len(data.split()))