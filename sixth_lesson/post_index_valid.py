import re

index = input()

pattern = r'\b\d{5}\b'

print(re.findall(pattern, index))