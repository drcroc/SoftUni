char = int(input())

for i in range(97, 97 + char):
    for j in range(97, 97 + char):
        for u in range(97, 97 + char):
            print(f'{chr(i)}{chr(j)}{chr(u)}')

