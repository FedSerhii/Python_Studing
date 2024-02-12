import re

date = input()

pattern = r'\d{2}\-\d{2}\-\d{4}'

if re.match(pattern, date):
    print('Valid')
else:
    print('Not Valid')