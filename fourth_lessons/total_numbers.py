numbers = list(range(1, 101))
total = 0
for i in numbers:
    total += i
    if total % 3 == 0 and total % 5 != 0:
        print(total)
