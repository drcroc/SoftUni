#   Write a program that keeps all the unique chemical elements.
#   On the first line, you will be given a number n - the count of input lines that you will receive.
#   On the following n lines, you will be receiving chemical compounds separated by a single space.
#   Your task is to print all the unique ones on separate lines (the order does not matter)

Lines = int(input())
elements = set()


for _ in range(Lines):
    names = input().split()
    for element in names:
        elements.add(element)

print('\n'.join(elements))
