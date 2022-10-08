from functools import reduce

expression = input().split()
nums = []

for char in expression:
    if char.lstrip('-').isnumeric():
        nums.append(int(char))

    else:
        if '+' == char:
            nums = [reduce(lambda x, y: x + y, nums)]

        elif '-' == char:
            nums = [reduce(lambda x, y: x - y, nums)]

        elif '*' == char:
            nums = [reduce(lambda x, y: x * y, nums)]

        elif '/' == char:
            nums = [reduce(lambda x, y: x // y, nums)]

print(*nums)
