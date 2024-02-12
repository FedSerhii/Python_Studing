import re

your_email = input()

pattern = r'[^@]+@[^@]+\.[^@]+'

if re.match(pattern, your_email):
    print('Valid')
else:
    print('Not Valid')
