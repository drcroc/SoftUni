# You are given a secret message you should decipher. To do that, you need to know that in each word:
#     • the second and the last letter are switched (e.g., Holle means Hello)
#     • the first letter is replaced by its character code (e.g., 72 means H)


def decipher(text):
    deciphered = []
    for i in range(len(text)):
        digit = ''
        letter = ''
        word = text[i]
        for character in word:
            if character.isdigit():
                digit += character
                letter = chr(int(digit))

            else:
                word = word.replace(digit, '')
                if not len(word) == 1:
                    word = word[-1:] + word[1:-1] + word[:1]
                break
        deciphered.append(letter + word)
    return deciphered


text_as_list = str(input()).split()

print(' '.join(decipher(text_as_list)))
