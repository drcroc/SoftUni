# Да се напише програма, в която потребителят въвежда вида и размерите на геометрична фигура и пресмята лицето й.
# Фигурите са четири вида: квадрат (square), правоъгълник (rectangle), кръг (circle) и триъгълник (triangle).
# На първия ред на входа се чете вида на фигурата
# (текст със следните възможности: square, rectangle, circle или triangle).
# ⦁	Ако фигурата е квадрат (square): на следващия ред се чете едно дробно число - дължина на страната му
# ⦁	Ако фигурата е правоъгълник (rectangle): на следващите два реда четат две дробни числа - дължините на страните му
# ⦁	Ако фигурата е кръг (circle): на следващия ред чете едно дробно число - радиусът на кръга
# ⦁	Ако фигурата е триъгълник (triangle): на следващите два реда четат две дробни числа
# - дължината на страната му и дължината на височината към нея
# Резултатът да се закръгли до 3 цифри след десетичната запетая.

from math import pi

type_of_figur = str(input())

if type_of_figur == 'square':
    x = float(input())
    square_area = x ** 2
    print('%.3f' % square_area)

elif type_of_figur == 'rectangle':
    x = float(input())
    y = float(input())
    rectangle_area = x * y
    print('%.3f' % rectangle_area)

elif type_of_figur == 'circle':
    x = float(input())
    circle_area = pi * x ** 2
    print('%.3f' % circle_area)
else:
    x = float(input())
    y = float(input())
    triangle_area = (x * y) / 2
    print('%.3f' % triangle_area)

