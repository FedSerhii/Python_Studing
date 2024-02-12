import re

my_string = input()

pattern = r'\b[A-Z][a-z]*\b'

if re.fullmatch(pattern, my_string):
    print('Valid')
else:
    print('Not Valid')
