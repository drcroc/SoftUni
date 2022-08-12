import re

pattern = r'[>]{2}([\w]+)[<]{2}(\d+[.]?\d+)[!]{1}(\d+)'
total = 0
products = []

while True:
    line = input()

    if line == 'Purchase':
        break

    product = re.finditer(pattern, line)
    for results in product:
        if product:
            products.append(results[1])
            total += float(results[2]) * float(results[3])

print(f'Bought furniture:')
for brought in products:
    print(brought)

print(f'Total money spend: {total:.2f}')


