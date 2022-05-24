import math
number = int(input())
end = 0
for a in range(1, 9):
    for b in range(9, a, -1):
        for c in range(0, 9):
            for d in range(9, c, -1):
                suma = a + b + c + d
                mutt = a * b * c * d
                if math.floor(mutt / suma) == 3:
                    if (number % 3) == 0:
                        print(f'{d}{c}{b}{a}')
                        end = 1
                        break
                if suma == mutt:
                    if (number % 10) == 5:
                        print(f'{a}{b}{c}{d}')
                        end = 1
                        break

                if end == 1:
                    break
            if end == 1:
                break
        if end == 1:
            break
    if end == 1:
        break

if end != 1:
    print(f'Nothing found')


