import re

phone_number = input()

pattern = r'\+\d{3}\s\d{2}\s\d{3}\-\d{4}'

if re.match(pattern, phone_number):
    print('Valid')
else:
    print('Not Valid')