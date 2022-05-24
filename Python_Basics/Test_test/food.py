# Вход:
# От конзолата се четат пет реда:
#  Първи ред – брой дни, в които Дядо Коледа отсъства – цяло число в интервала [1…5000]
#  Втори ред – оставена храна в килограми – цяло число в интервала [0…100000]
#  Трети ред – храна на ден за първия елен в килограми – реално число в интервала [0.00…100.00]
#  Четвърти ред – храна на ден за втория елен в килограми– реално число в интервала [0.00…100.00]
#  Пети ред – храна на ден за третия елен в килограми – реално число в интервала [0.00…100.00]
# Изход:
# На конзолата трябва да се отпечата на един ред:
#  Ако оставената храна Е достатъчна:
# o “{килограми, които остават} kilos of food left.”
#  Резултатът трябва да е закръглен към ПО-МАЛКОТО цяло число
#  Ако оставената храна НЕ Е достатъчна:
# o “{килограми, които не недостигат} more kilos of food are needed.”
#  Резултатът трябва да е закръглен към ПО-ГОЛЯМОТО цяло число
import math

days = int(input())
food = float(input())
f_deer = float(input())
s_deer = float(input())
t_deer = float(input())

eaten = (f_deer + s_deer + t_deer) * days
if eaten >= food:
    print(f'{math.ceil(abs(food - eaten))} more kilos of food are needed.')
else:
    print(f'{math.floor(abs(food - eaten))} kilos of food left.')










