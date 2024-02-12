import re

word = input()

patern = r'^[a-zA-Z]+$'

if re.match(patern, word):
    print('Valid')
else:
    print('Not Valid')