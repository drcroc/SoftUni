Lines = int(input())

intersection = list()

for _ in range(Lines):
    range_one, range_two = input().split('-')
    set_one, set_two = set(), set()
    range_one = [int(x) for x in range_one.split(',')]
    range_two = [int(x) for x in range_two.split(',')]

    # print(range_one, range_two)

    for i in range(range_one[0], range_one[-1]+1):
        set_one.add(i)

    for i in range(range_two[0], range_two[-1]+1):
        set_two.add(i)

    intersection_set = list(set_one & set_two)
    if len(intersection_set) > len(intersection):
        intersection = list(intersection_set)

print(f'Longest intersection is {intersection} with length {len(intersection)}')

