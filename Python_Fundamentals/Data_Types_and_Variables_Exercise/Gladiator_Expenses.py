
lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

shield_broken_count = 0
expenses = 0.00

for lost in range(1, lost_fights + 1):

    if lost % 2 == 0:
        expenses += helmet_price

    if lost % 3 == 0:
        expenses += sword_price

    if lost % 3 == 0 and lost % 2 == 0:
        expenses += shield_price
        shield_broken_count += 1

    if shield_broken_count == 2:
        expenses += armor_price
        shield_broken_count = 0

print(f"Gladiator expenses: {expenses:.2f} aureus")
