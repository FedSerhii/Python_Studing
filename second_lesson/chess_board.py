a = int(input('First of two for first: '))
b = int(input('Second of two for first: '))

a1 = int(input('First of two for second: '))
b1 = int(input('Second of two for second: '))

if (a + b) % 2 == 0 and (a1 + b1) % 2 == 0 or (a + b) % 2 != 0 and (a1 + b1) % 2 != 0:
    print('YES')
else:
    print('NO')
