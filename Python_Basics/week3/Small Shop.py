# Предприемчив българин отваря квартални магазинчета в няколко града и продава на различни цени според града:
# град / продукт
# Напишете програма, която чете продукт (текст), град (текст) и количество (десетично число),
# въведени от потребителя,
# и пресмята и отпечатва колко струва съответното количество от избрания продукт в посочения град.
# град / продукт    # Sofia     # Plovdiv       # Varna
# coffee            # 0.50      # 0.40          # 0.45
# water             # 0.80      # 0.70          # 0.70
# beer              # 1.20      # 1.15          # 1.10
# sweets            # 1.45      # 1.30          # 1.35
# peanuts           # 1.60      # 1.50          # 1.55

i = 0

price_c = [0.50, 0.40, 0.45]
price_w = [0.80, 0.70, 0.70]
price_b = [1.20, 1.15, 1.10]
price_s = [1.45, 1.30, 1.35]
price_p = [1.60, 1.50, 1.55]

drink = str(input())
city = str(input())
count = float(input())

if city == 'Sofia':
    i = 0
elif city == 'Plovdiv':
    i = 1
elif city == 'Varna':
    i = 2
else:
    print('Error')

if drink == 'coffee':
    coffee = count * price_c[i]
    print(coffee)
elif drink == 'water':
    water = count * price_w[i]
    print(water)
elif drink == 'beer':
    beer = count * price_b[i]
    print(beer)
elif drink == 'sweets':
    sweets = count * price_s[i]
    print(sweets)
elif drink == 'peanuts':
    peanuts = count * price_p[i]
    print(peanuts)
else:
    print('Error')
