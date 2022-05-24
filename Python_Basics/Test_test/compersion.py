# От конзолата се четат 4 реда:
# 1. Брой танцьори – цяло число в интервала [1 … 10]
# 2. Брой точки – реално число в интервала [1.00 … 10000.00]
# 3. Сезон – текст със следните възможности - "summer" или "winter"
# 4. Място – текст със следните възможности - "Bulgaria" или "Abroad"
# Изход:
# На конзолата се отпечатват 2 реда:
#  Сумата, която са дали за благотворителност
# "Charity - {сума за благотворителност}"
#  Сумата, която е получил всеки танцьор
# "Money per dancer - {сума за танцьор}"
# Сумите да бъдат форматирани до втория знак след десетичната запетая.


dancers = int(input())
points = float(input())
season = str(input())
place = str(input())

price = dancers * points
if place != 'Bulgaria':
    price = price + (price * 0.5)
    if season == 'winter':
        price = price - price * 0.15
    else:
        price = price - price * 0.10
else:
    if season == 'winter':
        price = price - price * 0.08
    else:
        price = price - price * 0.05

charity = price * 0.75
for_dancers = (price - charity) / dancers
print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {for_dancers:.2f}")

