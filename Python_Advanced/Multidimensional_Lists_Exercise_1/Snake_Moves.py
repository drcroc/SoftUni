from collections import deque

Rows, Columns = map(int, input().split(' '))
word = input()

idx = 0

for row in range(Rows):
    result = deque()
    for col in range(Columns):
        if idx == len(word):
            idx = 0
        if row % 2 == 0:
            result.append(word[idx])
        else:
            result.appendleft(word[idx])
        idx += 1
    print(''.join(result))
