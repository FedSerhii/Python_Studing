my_list = [123, 2, 23, 4, 23, 1, 22, 54]

min_element = my_list[0]
for i in my_list:
    if i < min_element:
        min_element = i

my_list.remove(min_element)

second_min_element = my_list[0]
for i in my_list:
    if i < second_min_element:
        second_min_element = i

print(f'Minimum element is {second_min_element}')
