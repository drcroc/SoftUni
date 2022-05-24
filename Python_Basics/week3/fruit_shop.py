work_fruit = [2.50, 1.20, 0.85, 1.45, 2.70, 5.50, 3.85]
week_fruit = [2.70, 1.25, 0.90, 1.60, 3.00, 5.60, 4.20]
work_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
week_day = ['Saturday', 'Sunday']
fruit_list = ['banana', 'apple', 'orange', 'grapefruit', 'kiwi', 'pineapple', 'grapes']

fruit = str(input())
day = str(input())
count = float(input())
if fruit in fruit_list:
    if day in work_day:
        if fruit == 'banana':
            price = work_fruit[0] * count
        elif fruit == 'apple':
            price = work_fruit[1] * count
        elif fruit == 'orange':
            price = work_fruit[2] * count
        elif fruit == 'grapefruit':
            price = work_fruit[3] * count
        elif fruit == 'kiwi':
            price = work_fruit[4] * count
        elif fruit == 'pineapple':
            price = work_fruit[5] * count
        else:
            price = work_fruit[6] * count
        print(f'{price:.2f}')
    elif day in week_day:
        if fruit == 'banana':
            price = week_fruit[0] * count
        elif fruit == 'apple':
            price = week_fruit[1] * count
        elif fruit == 'orange':
            price = week_fruit[2] * count
        elif fruit == 'grapefruit':
            price = week_fruit[3] * count
        elif fruit == 'kiwi':
            price = week_fruit[4] * count
        elif fruit == 'pineapple':
            price = week_fruit[5] * count
        else:
            price = week_fruit[6] * count
        print(f'{price:.2f}')
    else:
        print('error')
else:
    print('error')


