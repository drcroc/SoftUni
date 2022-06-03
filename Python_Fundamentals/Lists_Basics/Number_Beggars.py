money = str(input())
beggars = int(input())
suma_list = []

money_list = money.split(', ')
for i in range(0, beggars):
    suma = 0
    for j in range(0, len(money_list)):
        if i >= len(money_list):
            break
        suma += int(money_list[i])
        i += beggars

    suma_list.append(suma)

print(f'{suma_list}')
