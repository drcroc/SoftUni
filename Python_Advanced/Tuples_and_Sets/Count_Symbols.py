#   Write a program that reads a text from the console and counts the occurrences of each character in it.
#   Print the results in alphabetical (lexicographical) order.

text = [i for i in input()]
text.sort()
occurrences = dict()

for symbol in text:
    if symbol not in occurrences:
        occurrences[symbol] = 0
    occurrences[symbol] += 1

for keys, values in occurrences.items():
    print(f'{keys}: {values} time/s')
