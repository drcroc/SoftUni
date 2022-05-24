# Напишете програма, която чете цяло число, въведено от потребителя, и отпечатва ден от седмицата (на английски език),
# в граници [1...7] или отпечатва "Error" в случай, че въведеното число е невалидно.

num_day = int(input())

if 0 < num_day < 8:
    if num_day == 1:
        print("Monday")
    elif num_day == 2:
        print("Tuesday")
    elif num_day == 3:
        print("Wednesday")
    elif num_day == 4:
        print("Thursday")
    elif num_day == 5:
        print("Friday")
    elif num_day == 6:
        print("Saturday")
    else:
        print("Sunday")
else:
    print("Error")