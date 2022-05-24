num_c = int(input())
left = int()
right = int()
for i in range(num_c*2):
    number = int(input())
    if i < num_c:
        left += number
    else:
        right += number

if left == right:
    print('Yes, sum =', left)
else:
    print('No, diff =', abs(left - right))












# from math import ceil
#
# n = int(input())
# m = list()
# sum_mer = list()
# i = 0
# for i in range(2*n):
#     k = int(input())
#     m.append(k)
#     #print(m)
# y, b = 0, 0
# for y in range(n):
#     z = m[b] + m[b+1]
#     b += 2
#     sum_mer.append(z)
#
# u = 0
#
# c = ceil(n/2)
#
# for u in range(c):
#     if (sum_mer[u] - sum_mer[u + 1]) != 0:
#         print('No, diff =', abs(sum_mer[u] - sum_mer[u + 1]))
#     else:
#         print('Yes, sum =', abs(sum_mer[u]))
