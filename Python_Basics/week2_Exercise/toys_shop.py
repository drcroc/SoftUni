# Петя има магазин за детски играчки. Тя получава голяма поръчка, която трябва да изпълни.
# С парите, които ще спечели иска да отиде на екскурзия.
# Цени на играчките:

# Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена.
# От спечелените пари Петя трябва да даде 10% за наема на магазина.
# Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.
# Вход
# От конзолата се четат 6 реда:
#     1. Цена на екскурзията - реално число в интервала [1.00 … 10000.00]
#     2. Брой пъзели - цяло число в интервала [0… 1000]
#     3. Брой говорещи кукли - цяло число в интервала [0 … 1000]
#     4. Брой плюшени мечета - цяло число в интервала [0 … 1000]

trip = float(input())
puzzle = int(input())
talking_doll = int(input())
teddy_bare = int(input())
minion = int(input())
truck = int(input())

puzzle_price = 2.60 * puzzle
talking_doll_price = 3.00 * talking_doll
teddy_bare_price = 4.10 * teddy_bare
minion_price = 8.20 * minion
truck_price = 2 * truck

all_toys = puzzle + talking_doll + teddy_bare + minion + truck
total_with_out_off = puzzle_price + talking_doll_price + teddy_bare_price + minion_price + truck_price
if all_toys >= 50:
    total_with_off = total_with_out_off - total_with_out_off*(1/4)
    profit = total_with_off - total_with_off*(1/10)
else:
    profit = total_with_out_off-total_with_out_off*(1/10)

money = profit - trip

if money >= 0:
    print(f"Yes! {abs(money):.2f} lv left.")
else:
    print(f"Not enough money! {abs(money):.2f} lv needed.")


