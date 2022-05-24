# Напишете програма която, чете ден от седмицата (текст), на английски език - въведен от потребителя.
# Ако денят е работен отпечатва на конзолата - "Working day", ако е почивен - "Weekend".
# Ако се въведе текст различен от ден от седмицата да се отпечата - "Error".

day_str = str(input())
Working_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
Weekend = ['Saturday', 'Sunday']

if day_str in Working_day:
    print('Working day')
elif day_str in Weekend:
    print('Weekend')
else:
    print('Error')



# Monday
# Tuesday
# Wednesday
# Thursday
# Friday
# Saturday
# Sunday
