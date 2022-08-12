# Type              Maximum Price
# Clothes           50.00
# Shoes             35.00
# Accessories       20.50

items_price = input().split('|')
budget = float(input())

profit, new_budget = 0, 0

for items in items_price:
    product, price = items.split('->')
    price = float(price)
    if budget >= price:
        if any(['Clothes' in product and price <= 50.00,
                'Shoes' in product and price <= 35.00,
                'Accessories' in product and price <= 20.50]):
            sold_profit = price * 0.40
            profit += sold_profit
            new_budget += sold_profit + price
            budget -= price
            print(f'{sold_profit + price:.2f}', end=' ')

print(f'\nProfit: {profit:.2f}')
if new_budget + budget >= 150:
    print(f'Hello, France!')
else:
    print(f'Not enough money.')















