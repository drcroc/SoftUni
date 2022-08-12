import re

# a - 97 z - 122

pattern = r'(\w)(\d+)(\w)'
total, num = 0.00, 0.00

variable = re.findall(pattern, input())
for var in variable:
    front, num, back = var[0], float(var[1]), var[-1]

    if front.isupper():   # divide
        num = num / (ord(front.lower()) - 96)
    else:               # multiply
        num = num * (ord(front.lower()) - 96)

    if back.isupper():    # subtract
        num = num - (ord(back.lower()) - 96)
    else:               # add
        num = num + (ord(back.lower()) - 96)

    total += num

print(f'{total:.2f}')
