m = int(input('Please enter the number of horizontal cubes: '))
n = int(input('Please enter the number of vertical cubes: '))
k = int(input('Please enter the number of desired cubes: '))

if k % n == 0 or k % m == 0:
    print('Yes')
else:
    print('No')