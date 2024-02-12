n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def create_phone_number(n):
    result1 = ''.join(str(i) for i in n[0:3])
    result2 = ''.join(str(i) for i in n[3:6])
    result3 = ''.join(str(i) for i in n[6:10])

    phone_number = f'({result1}) {result2}-{result3}'

    return phone_number


print(create_phone_number(n))
