locations = int(input())
total = 0

for loc in range(locations, 0, -1):
    expected_daily = int(input())
    days = int(input())
    total = 0
    for day in range(days, 0, -1):
        daily = int(input())
        total = total + daily

    average = total / days
    if average >= expected_daily:
        print(f'Good job! Average gold per day: {average:.2f}.')
    else:
        print(f'You need {(expected_daily - average):.2f} gold.')


















