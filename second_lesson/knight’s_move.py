a = int(input('First of two for first: '))
b = int(input('Second of two for first: '))

a1 = int(input('First of two for second: '))
b1 = int(input('Second of two for second: '))

if abs(a - a1) == 1 and abs(b - b1) == 2 or abs(a - a1) == 2 and abs(b - b1) == 1:
    print('Yes')
else:
    print('No')