import re

pattern = r'(\d+)'
numbers = []
while True:
    line = input()

    if line:
        numbers = re.findall(pattern, line)
        for num in numbers:
            print(num, end=' ')

    else:
        break


