# Румен иска да пребоядиса хола и за целта е наел майстори.
# Напишете програма, която изчислява разходите за ремонта, предвид следните цени:
#     • Предпазен найлон - 1.50 лв. за кв. метър
#     • Боя - 14.50 лв. за литър
#     • Разредител за боя - 5.00 лв. за литър
# За всеки случай, към необходимите материали,
# Румен иска да добави още 10% от количеството боя и 2 кв.м. найлон, разбира се и 0.40 лв. за торбички.
# Сумата, която се заплаща на майсторите за 1 час работа, е равна на 30% от сбора на всички разходи за материали.
# Вход
# Входът се чете от конзолата и съдържа точно 4 реда:
#     1. Необходимо количество найлон (в кв.м.) - цяло число в интервала [1... 100]
#     2. Необходимо количество боя (в литри) - цяло число в интервала [1…100]
#     3. Количество разредител (в литри) - цяло число в интервала [1…30]
#     4. Часовете, за които майсторите ще свършат работата - цяло число в интервала [1…9]

nylon_sqr_meter_price = 1.50
paint_lit_price = 14.50
thinner_lit_price = 5.00
bags = 0.40

nylon_sqr_meter = int(input())
paint_lit = int(input())
thinner_lit = int(input())
hours = int(input())

needed_nylon_sqr_meter_price = (nylon_sqr_meter + 2) * nylon_sqr_meter_price
needed_paint_price = (paint_lit + (paint_lit * 10 / 100 )) * paint_lit_price
needed_thinner_price = thinner_lit * thinner_lit_price
supply_cost = needed_nylon_sqr_meter_price + needed_paint_price + needed_thinner_price + bags
job_cost_for_hour = supply_cost * (30 / 100)

total_cost_for_labor = job_cost_for_hour * hours
total_cost = supply_cost + total_cost_for_labor

print(total_cost)

