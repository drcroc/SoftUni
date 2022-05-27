# You will receive N – an integer, the number of snowballs being made by Tony and Andi.
# On the following lines, you will receive 3 inputs for each snowball:
#     • The weight of the snowball (integer).
#     • The time needed for the snowball to get to its target (integer).
#     • The quality of the snowball (integer).
# For each snowball, you must calculate its value by the following formula:
# (snowball_weight / snowball_time) ** snowball_quality
# In the end, you must print the highest calculated value of a snowball.

snowball = int(input())
weight = []
time = []
quality = []
points = 0
top = 0

for i in range(0, snowball):
    weight.append(int(input()))
    time.append(int(input()))
    quality.append(int(input()))

    if (weight[i] / time[i]) ** quality[i] > points:
        points = int((weight[i] / time[i])) ** quality[i]
        top = i
print(f'{weight[top]} : {time[top]} = {points} ({quality[top]})')



