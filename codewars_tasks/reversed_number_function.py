def digitize(n):
     return [int(digit) for digit in reversed(str(n))]


print(digitize(35231))