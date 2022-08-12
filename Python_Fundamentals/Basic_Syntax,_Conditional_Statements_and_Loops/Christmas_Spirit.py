# Decoration    Price/Piece     Points/Shopping
# Ornament Set  2$              5
# Tree Skirt    5$              3
# Tree Garland  3$              10
# Tree Lights   15$             17


piece = int(input())
days_until_Christmas = int(input())

budget = 0
totalSpirit = 0
day = 1

for day in range(1, days_until_Christmas + 1):
    if day % 11 == 0:
        piece += 2

    if day % 2 == 0:  # buy Ornament Sets
        totalSpirit += 5
        budget += piece * 2

    if day % 3 == 0:  # buy Tree Skirts and Tree Garlands
        totalSpirit += 13
        budget += piece * 8

    if day % 5 == 0:  # buy Tree Lights
        if day % 3 == 0:
            totalSpirit += 30
        totalSpirit += 17
        budget += piece * 15

    if day % 10 == 0:  # cat ruins decoration
        totalSpirit -= 20
        budget += 23

if day % 10 == 0:
    totalSpirit -= 30


print(f"Total cost: {budget}")
print(f"Total spirit: {totalSpirit}")
