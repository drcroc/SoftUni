N_line = int(input())

even_total, odd_total = 0, 0

odd, even, number = set(), set(), list()

for i in range(1, N_line + 1):
    name, num = input(), 0

    for char in name:
        num += ord(char)

    num = num // i

    if num % 2 == 0:
        even.add(num)
    else:
        odd.add(num)

even_total, odd_total = sum(even), sum(odd)


if even_total > odd_total:
    print(*(even.symmetric_difference(odd)), sep=', ')

elif odd_total > even_total:
    print(*(odd.difference(even)), sep=', ')

else:
    print(*(odd.union(even)), sep=', ')
