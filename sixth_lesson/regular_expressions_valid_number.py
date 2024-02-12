import re

numbers = input()

pattern = r'^\d+$'

if re.match(pattern, numbers):
    print('Valid')
else:
    print('Not valid')