# Снимките за дългоочаквания филм "Годзила срещу Конг" започват.
# Сценаристът Адам Уингард ви моли да напишете програма,
# която да изчисли, дали предвидените средства са достатъчни за снимането на филма.
# За снимките  ще бъдат нужни определен брой статисти, облекло за всеки един статист и декор.
# Известно е, че:
#         ◦ Декорът за филма е на стойност 10% от бюджета.
#         ◦ При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.
# Вход
# От конзолата се четат 3 реда:
#     Ред 1. Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
#     Ред 2. Брой на статистите – цяло число в интервала [1 … 500]
#     Ред 3. Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]

budget = float(input())
statist = int(input())
price_of_clouts = float(input())

if statist > 150:
    price_of_clouts_final = statist * (price_of_clouts*(9/10))
else:
    price_of_clouts_final = statist * price_of_clouts

decor = budget * 1/10

total = budget - (decor + price_of_clouts_final)

if total >= 0:
    print('Action!')
    print(f'Wingard starts filming with {abs(total):.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {abs(total):.2f} leva more.')





