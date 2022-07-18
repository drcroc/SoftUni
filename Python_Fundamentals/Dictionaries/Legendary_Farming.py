
materials = {'shards': 0, 'fragments': 0, 'motes': 0}

obtained = False

entry = input().split()

while not obtained:
    for i in range(0, len(entry), 2):
        value = int(entry[i])
        key = entry[i + 1].lower()

        if key not in materials.keys():
            materials[key] = 0
        materials[key] += value

        if materials['shards'] >= 250:
            print('Shadowmourne obtained!')
            materials['shards'] -= 250
            obtained = True

        elif materials['fragments'] >= 250:
            print('Valanyr obtained!')
            materials['fragments'] -= 250
            obtained = True

        elif materials['motes'] >= 250:
            print('Dragonwrath obtained!')
            materials['motes'] -= 250
            obtained = True

        if obtained:
            break

    if obtained:
        break

    entry = str(input()).split()

for material, quantity in materials.items():
    print(f"{material}: {quantity}")

# 3 Motes 5 stones 5 Shards 6 leathers 255 fragments 7 Shards
# 123 silver 6 shards 8 shards 5 motes 9 fangs 75 motes 103 MOTES 8 Shards 86 Motes 7 stones 19 silver
