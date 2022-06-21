# You will be given two sequences of strings, separated by ", ".
# Print a new list containing only the strings from the first input line,
# which are substrings of any string in the second input line.

# arp, live, strong                             ['arp', 'live', 'strong']
# lively, alive, harp, sharp, armstrong

# tarp, mice, bull                               []
# lively, alive, harp, sharp, armstrong


main_str = str(input()).split(', ')
second_str = str(input()).split()
word_in = []

for i in range(0, len(main_str)):
    for word in second_str:
        if main_str[i] in word:
            word_in.append(main_str[i])
            break

print(word_in)










