constraints = input().split('|')

coins = 100
energy = 100
managed = True

for items in constraints:

    if not managed:
        break

    event_ingredient, number = items.split('-')
    number = int(number)

    if 'rest' == event_ingredient:
        if energy + number > 100:
            print(f"You gained {abs(100 - energy)} energy.")
            energy = 100

        else:
            energy += number
            print(f'You gained {number} energy.')

        print(f'Current energy: {energy}.')

    elif 'order' == event_ingredient:
        if energy >= 30:
            energy -= 30
            coins += number
            print(f'You earned {number} coins.')

        else:
            energy += 50
            print(f'You had to rest!')

    else:
        if coins >= number:
            coins -= number
            print(f'You bought {event_ingredient}.')

        else:
            print(f'Closed! Cannot afford {event_ingredient}.')
            managed = False
            break

if managed:
    print(f'Day completed!'
          f'\nCoins: {coins}'
          f'\nEnergy: {energy}')
