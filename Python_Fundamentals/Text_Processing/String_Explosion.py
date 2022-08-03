line = input().split('>')

result = ''
power = 0

for word in line:
    if len(word) > 1 and any(map(str.isdigit, word)):
        power += (int(word[0]) - 1)
        if power > len(word):
            result += '>'

        else:
            result += '>' + word[1 + power:]
            power = 0

    elif len(word) == 1 and word.isdigit():
        if int(word):
            power += (int(word) - 1)
        result += '>'
    else:
        result += word

print(result)

