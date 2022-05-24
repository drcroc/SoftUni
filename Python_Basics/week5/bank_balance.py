balance = float()
enter = 1
while enter != 'NoMoreMoney':
    enter = input()
    if enter != 'NoMoreMoney':
        if float(enter) < 0:
            enter = 'NoMoreMoney'
            print('Invalid operation!')
            break
        else:
            print(f'Increase: {float(enter):.2f}')
            balance = balance + float(enter)
    else:
        break


print(f'Total: {balance:.2f}')
