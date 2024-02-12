my_string = 'Hello'
my_set = set()

for i in my_string:
    if i not in my_set:
        print(f'{i} = {my_string.count(i)}')
        my_set.add(i)
