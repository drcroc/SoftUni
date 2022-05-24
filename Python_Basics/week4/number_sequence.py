n = int(input())
m = int(input())
max_num = m
min_num = m
for i in range(n-1):
    m = int(input())
    if max_num < m:
        max_num = m
    else:
        if min_num > m:
            min_num = m

print('Max number:', max_num)
print('Min number:', min_num)

