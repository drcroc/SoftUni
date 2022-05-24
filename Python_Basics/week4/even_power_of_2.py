x = 1
n = int(input())

for n in range(n+1):
    if not n % 2:
        x = 2**n
        print(x)
