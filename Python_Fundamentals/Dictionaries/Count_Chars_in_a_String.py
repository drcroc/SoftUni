# Write a program that counts all characters in a string except for space (" ").
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"

string = ''.join(s for s in input().split())
letters = dict()

for char in string:
    if char not in letters.keys():
        letters[char] = 0
    letters[char] += 1
for key, value in letters.items():
    print(f'{key} -> {value}')

















