pastry = str(input())
count = int(input())
day = int(input())

if pastry == 'Cake':
    if day <= 15:
        price = count * 24
    else:
        price = count * 28.70

elif pastry == 'Souffle':
    if day <= 15:
        price = count * 6.66
    else:
        price = count * 9.80

else:
    if day <= 15:
        price = count * 12.60
    else:
        price = count * 16.98

if day <= 22:
    if price > 200:
        price = price - (price * 0.25)
    elif 100 <= price <= 200:
        price = price - (price * 0.15)

if day <= 15:
    price = price - (price * 0.10)

print(f'{price:.2f}')



