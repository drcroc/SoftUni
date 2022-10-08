from collections import deque

materials = list(map(int, input().split()))
magics = deque(map(int, input().split()))

crafted = dict()
level = 0

while materials and magics:
    material, magic = materials.pop(), magics.popleft()
    flag = False
    if materials == 0 and magic == 0:
        continue

    if magic == 0:
        materials.append(material)
        continue

    if materials == 0:
        magics.appendleft(magic)
        continue

    level = material * magic

    if level < 0:
        mater = material + magic
        materials.append(mater)

    elif 150 == level:
        if 'Doll' not in crafted.keys():
            crafted['Doll'] = 0
        crafted['Doll'] += 1

    elif 250 == level:
        if 'Wooden train' not in crafted.keys():
            crafted['Wooden train'] = 0
        crafted['Wooden train'] += 1

    elif 300 == level:
        if 'Teddy bear' not in crafted.keys():
            crafted['Teddy bear'] = 0
        crafted['Teddy bear'] += 1

    elif 400 == level:
        if 'Bicycle' not in crafted.keys():
            crafted['Bicycle'] = 0
        crafted['Bicycle'] += 1

    else:
        materials.append(material + 15)

    if 'Doll' in crafted.keys() and 'Wooden train' in crafted.keys():
        task = True

    if 'Teddy bear' in crafted.keys() and 'Bicycle' in crafted.keys():
        task = True

if 'Doll' in crafted.keys() and 'Wooden train' in crafted.keys() or 'Teddy bear' in \
        crafted.keys() and 'Bicycle' in crafted.keys():
    print(f'The presents are crafted! Merry Christmas!')
else:
    print(f'No presents this Christmas!')

if materials:
    print(f'Materials left:', ', '.join(map(str, reversed(materials))))
else:
    print(f'Magic left:', ', '.join(map(str, magics)))

if crafted:
    for key, items in sorted(crafted.items()):
        print(f'{key}: {items}')
