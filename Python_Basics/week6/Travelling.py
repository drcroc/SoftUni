destination = str()
budget = float()
saves = 0.00

while True:
    destination = str(input())
    if destination == 'End':
        break

    budget = float(input())
    saves = 0.00
    while saves < budget:
        saved = float(input())
        saves += saved

    print(f'Going to {destination}!')




