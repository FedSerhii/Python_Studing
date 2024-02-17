a = int(input('First of two for first: '))
b = int(input('Second of two for first: '))

a1 = int(input('First of two for second: '))
b1 = int(input('Second of two for second: '))

if abs(a - a1) == 1 and abs(b - b1) == 1:
    print('Yes')
elif abs(a - a1) == 0 and abs(b - b1) == 1 or abs(a - a1) == 1 and abs(b - b1) == 0:
    print('Yes')
else:
    print('No')