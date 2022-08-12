# Eggs - 1 pack
# Flour - 1 kg
# Milk - 0.250 l

budget = float(input())
price_flour = float(input())
eggs = price_flour * 0.75
milk = price_flour + price_flour * 0.25

current_bread_count = 0
total = 0
colored_eggs = 0

price_loaves_bread = price_flour + eggs + milk * 0.25


while total + price_loaves_bread <= budget:
    current_bread_count += 1
    colored_eggs += 3
    total = current_bread_count * price_loaves_bread

    if current_bread_count % 3 == 0:
        colored_eggs -= current_bread_count - 2

budget_left = budget - total


print(f'You made {current_bread_count} loaves of Easter bread!'
      f' Now you have {colored_eggs} eggs and {budget_left:.2f}BGN left.')

