import math
other_parts = 1000
price_gpu = float(input())
price_cable = float(input())
price_elect = float(input())
prof_gpu = float(input())

total_cards = price_gpu * 13
total_cable = price_cable * 13
initial_price = total_cable + total_cards + other_parts
daily_prof = (prof_gpu - price_elect) * 13

return_of_invest = initial_price / daily_prof
print(math.ceil(initial_price))
print(math.ceil(return_of_invest))




