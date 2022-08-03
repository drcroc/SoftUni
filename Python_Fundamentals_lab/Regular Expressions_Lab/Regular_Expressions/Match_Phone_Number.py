import re

numbers = input()

pattern = r'\+359([ -])2\1([0-9]{3})\1([0-9]{4})\b'


# matches = ["".join(x) for x in re.findall(pattern, numbers)]
# print(', '.join(matches))
# matches = re.findall()
matches = ["".join(x.group()) for x in re.finditer(pattern, numbers)]
print(', '.join(matches))









