# x1 + x2 + x3 = n
n = int(input())
c = 0
for x1 in range(0, n+1):
    for x2 in range(0, n+1):
        for x3 in range(0, n+1):
            num = x1 + x2 + x3
            if num == n:
                c += 1
                break

print(c)

