my_list = input()

try:
    print(my_list[5])
except IndexError:
    print("This index doesn't exist")
