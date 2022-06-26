# flour
# 10 eggs
# apron
# budget
# student
# price of flour
# price of single egg
# price of apron +20% per student
# ({)f'Items purchased for {money}$.')
# {f'{needed_money}$ more needed'}
import math

budget = float(input())
students = int(input())
price_of_flour = float(input())
price_of_single_egg = float(input())
price_of_apron = float(input())
free_flour = students // 5
# int(- (-x // 1))
money = price_of_apron * (math.ceil(students + students * 0.2))
money += price_of_single_egg * 10 * students
money += price_of_flour * (students - free_flour)

if budget - money >= 0:
    print(f'Items purchased for {money:.2f}$.')
else:
    print(f'{(money - budget):.2f}$ more needed.')



