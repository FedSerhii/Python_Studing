n = int(input('Enter the number of minutes from the beginning of the day: '))

m = n % 60
h = n // 60

if h >= 24:
    h1 = h - 24
    print(f'Clock shows {h1} hours and {m} minutes')
else:
    print(f'Clock shows {h} hours and {m} minutes')