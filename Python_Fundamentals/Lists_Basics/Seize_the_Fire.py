fire_cell = input().split('#')
water = int(input())

total_fire, effort, water_left = 0, 0, water

print("Cells:")

for fire in fire_cell:

    fire_type, fire_range = [int(x) if x.isdigit() else x for x in fire.split(" = ")]
    if water_left >= fire_range:
        if fire_type == 'Low' and fire_range in range(1, 51):
            effort += fire_range * 0.25
            total_fire += fire_range
            water_left -= fire_range
            print(f' - {fire_range}')

        if fire_type == 'Medium' and fire_range in range(51, 81):
            effort += fire_range * 0.25
            total_fire += fire_range
            water_left -= fire_range
            print(f' - {fire_range}')

        if fire_type == 'High' and fire_range in range(81, 126):
            effort += fire_range * 0.25
            total_fire += fire_range
            water_left -= fire_range
            print(f' - {fire_range}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire:}')
