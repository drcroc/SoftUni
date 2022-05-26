fills = int(input())
tank = 0

for i in range(0, fills):
    entry = int(input())
    if entry + tank <= 255:
        tank += entry
    else:
        print(f'Insufficient capacity!')
        continue


print(f'{tank}')



