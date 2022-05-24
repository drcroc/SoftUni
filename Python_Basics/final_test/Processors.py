import math
badge = int(input())
workers = int(input())
days = int(input())
worked_hours = workers * days * 8
processors_made = math.floor(worked_hours / 3)

if badge <= processors_made:
    profit = (processors_made - badge) * 110.10
    print(f'Profit: -> {profit:.2f} BGN')
else:
    losses = (badge - processors_made) * 110.10
    print(f'Losses: -> {losses:.2f} BGN')
