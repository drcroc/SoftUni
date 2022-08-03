import re

date = input()

pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'


for x in re.finditer(pattern, date):
    print(x.group(), end=' ')
