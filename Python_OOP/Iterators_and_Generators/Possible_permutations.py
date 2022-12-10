from itertools import permutations


def possible_permutations(nums):
    output = permutations(nums)
    for permutation in output:
        yield list(permutation)




[print(n) for n in possible_permutations([1, 2, 3])]