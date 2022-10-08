from collections import deque

colony = deque(map(int, input().split()))
honey = list(map(int, input().split()))
symbols_list = deque(input().split())

total_honey = 0
while colony and honey:
    nectar, bees, symbols = honey.pop(), colony.popleft(), symbols_list.popleft()
    if nectar >= bees:
        if symbols == '+':
            total_honey += abs(bees + nectar)

        elif symbols == '-':
            total_honey += abs(bees - nectar)

        elif symbols == '*':
            total_honey += abs(bees * nectar)

        elif symbols == '/':
            total_honey += abs(bees / nectar)

    else:
        symbols_list.appendleft(symbols)
        colony.appendleft(bees)

print(f'Total honey made: {total_honey}')

if colony:
    print(f"Bees left: {', '.join(str(x) for x in colony)}")

if honey:
    print(f"Nectar left: {', '.join(str(x) for x in honey)}")
#
# if colony:
#     print(f'Bees left:', ', '.join(map(str, colony)))
# if honey:
#     print(f'Nectar left:', ', '.join(map(str, honey)))
