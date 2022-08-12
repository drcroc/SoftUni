import re

pattern = r'(@|#)+([a-z]{3,})(@|#)+(\!|\@|\#|\$|\%|\^|\&|\*|\(|\)|\-|\_|\=|\+)*(\/+)(\d+)(\/+)'

string = input()
variable = re.findall(pattern, string)
color, count = '', 0

for var in variable:
    for char in var:
        if char.isdigit():
            count = char
        elif char.isalpha():
            color = char
    print(f'You found {count} {color} eggs!')

