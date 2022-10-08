from collections import deque

chocolates = list(map(int, input().split(', ')))       # 20, 24, -5, 17, 22, 60, 26
cups_milk = deque(map(int, input().split(', ')))          # 26, 60, 22, 17, 24, 10, 55
milkshake = 0

while milkshake < 5 and cups_milk and chocolates:
    flag = False
    if chocolates[-1] <= 0:
        chocolates.pop()
        flag = True

    if cups_milk[0] <= 0:
        cups_milk.popleft()
        flag = True

    if flag:
        continue

    if chocolates[-1] == cups_milk[0]:
        milkshake += 1
        chocolates.pop()
        cups_milk.popleft()
    else:
        cups_milk.append(cups_milk.popleft())
        chocolates[-1] -= 5


if milkshake == 5:
    print(f'Great! You made all the chocolate milkshakes needed!')
else:
    print(f'Not enough milkshakes.')

if chocolates:
    print(f'Chocolate:', ', '.join(map(str, chocolates)))
else:
    print(f'Chocolate: empty')

if cups_milk:
    print(f'Milk:', ', '.join(map(str, cups_milk)))
else:
    print(f'Milk: empty')

