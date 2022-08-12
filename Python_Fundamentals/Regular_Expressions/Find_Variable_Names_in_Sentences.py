import re

pattern = r'\b[_]{1}([a-zA-Z0-9]+)\b'

line = input()

variable = re.findall(pattern, line)

print(','.join(variable))




