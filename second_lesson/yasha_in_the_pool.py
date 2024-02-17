n = int(input('Please enter the length of the side: '))
m = int(input('Please enter the length of the side: '))
x = int(input('Where is Yasha?: '))
y = int(input('Where is Yasha?: '))

if n > m:
    i = n
    s = m
else:
    i = m
    s = n

j = [i-y, s-x, x, y]
print(min(j))