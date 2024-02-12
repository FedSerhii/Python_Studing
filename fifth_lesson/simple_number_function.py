def simple_number(a):
    if a <= 1:
        return False
    elif a <= 3:
        return True

    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False

    return True


print(simple_number(17))
