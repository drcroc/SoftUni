def sorted_list(sort):
    return sorted(sort)


unsorted = str(input()).split(' ')
unsorted = [int(i) for i in unsorted]

print(sorted_list(unsorted))
