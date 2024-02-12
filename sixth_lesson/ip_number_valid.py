import re

ip_number = input()

pattern = r'\d{3}\.\d{3}\.\d{1}\.\d{1}'

if re.match(pattern, ip_number):
    print('Valid')
else:
    print('Not Valid')