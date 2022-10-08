#   Write a program that prints a set of elements.
#   On the first line, you will receive two numbers -
#   n and m, separated by a single space - representing the lengths of two separate sets.
#   On the next n + m lines, you will receive n numbers, which are the numbers in the first set, and m numbers,
#   which are in the second set.
#   Find all the unique elements that appear in both and print them on separate lines (the order does not matter).

N_lines, M_lines = [int(x) for x in input().split()]
n, m = set(), set()

for _ in range(N_lines):
    line = input()
    n.add(line)

for _ in range(M_lines):
    line = input()
    m.add(line)

print(f'\n'.join(n & m))

