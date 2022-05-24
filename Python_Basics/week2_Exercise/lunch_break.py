# По време на обедната почивка искате да изгледате епизод от своя любим сериал.
# Вашата задача е да напишете програма, с която ще разберете дали имате достатъчно време да изгледате епизода.
# По време на почивката отделяте време за обяд и време за отдих.
# Времето за обяд ще бъде 1/8 от времето за почивка, а времето за отдих ще бъде 1/4 от времето за почивка.
# Вход
# От конзолата се четат 3 реда:
#     1. Име на сериал – текст
#     2. Продължителност на епизод  – цяло число в диапазона [10… 90]
#     3. Продължителност на почивката  – цяло число в диапазона [10… 120]

import math

series = str(input())
ep_length = float(input())
free_time = float(input())

lunch_time = free_time * (1/8)
chill_time = free_time * (1/4)

free_time = free_time - (lunch_time + chill_time)

if ep_length > free_time:
    print(f"You don't have enough time to watch {series},"
          f" you need {math.ceil(abs(free_time - ep_length)):.0f} more minutes.")
else:
    print(f"You have enough time to watch {series} and left with {math.ceil(abs(ep_length - free_time)):.0f} minutes free time.")









