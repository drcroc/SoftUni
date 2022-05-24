orders = int(input())
total_price = 0

for i in range(orders):
    price_capsule = float(input())
    days = int(input())
    capsule_day = int(input())
    error = 0

    if not 0.01 <= price_capsule <= 100.00:
        error += 1
    if not 1 <= days <= 31:
        error += 1
    if not 1 <= capsule_day <= 2000:
        error += 1
    if error >= 1:
        continue

    price = (price_capsule * capsule_day) * days
    print(f'The price for the coffee is: ${price:.2f}')
    total_price = total_price + price

print(f'Total: ${total_price:.2f}')



