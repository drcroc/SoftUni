import re

pattern = r'([\D]+)(\d+)'

message = input()
txt, rage_txt = '', ''

variable = re.findall(pattern, message)

for words in variable:
    txt, n = words[0], words[-1]
    txt = txt.upper()
    for i in range(int(n)):
        rage_txt += txt

print(f'Unique symbols used: {len(set(rage_txt))}')
print(rage_txt, end='')
