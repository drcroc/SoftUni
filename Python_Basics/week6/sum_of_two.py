# enter range
x1 = int(input())
x2 = int(input())
magic_num = int(input())
counter = 0
combi = False
for i in range(x1, x2+1):
    for y in range(x1, x2+1):
        counter += 1
        if i + y == magic_num:
            combi = True
            break
    if combi:
        break


if combi:
    print(f'Combination N:{counter} ({i} + {y} = {magic_num})')
else:
    print(f'{counter} combinations - neither equals {magic_num}')
