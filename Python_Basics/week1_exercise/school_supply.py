# Учебната година вече е започнала и отговорничката на 10Б клас - Ани трябва да купи определен брой пакетчета с химикали
# , пакетчета с маркери, както и препарат за почистване на дъска.
# Тя е редовна клиентка на една книжарница, затова има намаление за нея,
# което представлява някакъв процент от общата сума.
# Напишете програма, която изчислява колко пари ще трябва да събере Ани,
# за да плати сметката, като имате предвид следния ценоразпис:
#     • Пакет химикали - 5.80 лв.
#     • Пакет маркери - 7.20 лв.
#     • Препарат - 1.20 лв (за литър)

pen_price = 5.80
marker_price = 7.20
chemical_price = 1.20

pen_total = int(input())
marker_total = int(input())
chemical_total = int(input())
off = int(input())

money_without_off = pen_total*pen_price + marker_total*marker_price + chemical_price*chemical_total
money_needed = money_without_off -(money_without_off*off/100)

print(f'{money_needed:.4}')

