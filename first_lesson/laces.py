a = int(input('Please enter opposite distance: '))
b = int(input('Please enter parallel distance: '))
L = int(input('Free length is: '))
N = int(input('The number of holes is: '))

long = (a * N + b * (N-1) + L) * 2 - a
print(f'Drawstring length is {long} cm')