factor = int(input())
count = int(input())
lis = []
num = 0

for i in range(0, count):
    num += factor
    lis.append(num)
print(f'{lis}')


