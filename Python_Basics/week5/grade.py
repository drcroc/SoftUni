name = str(input())
fail_counter = int()
enter = float()
avg = float()
grade = 1

while grade <= 12:
    enter = float(input())
    if enter < 4:
        fail_counter += 1
        if fail_counter == 2:
            break
        continue
    grade += 1
    avg += enter
if fail_counter >= 2:
    print(f'{name} has been excluded at {grade} grade')
else:
    print(f'{name} graduated. Average grade: {(avg / 12):.2f}')
