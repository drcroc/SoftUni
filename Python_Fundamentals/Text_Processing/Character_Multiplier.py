word_one_char, word_two_char = input().split(' ')
suma = 0

str1 = [ord(char) for char in word_one_char]
str2 = [ord(char) for char in word_two_char]

diff = abs(len(str1) - len(str2))

if len(str1) < len(str2):
    smallest = len(str1)
else:
    smallest = len(str2)

suma = sum([str1[i] * str2[i] for i in range(0, smallest)])

if diff > 0:
    if len(str1) < len(str2):
        suma += sum([str2[i] for i in range(len(str1), len(str2))])
    else:
        suma += sum([str1[i] for i in range(len(str2), len(str1))])

print(suma)


# word_one_char, word_two_char = input().split(' ')
# str1 = []
# str2 = []
# suma = 0
#
# for char in word_one_char:
#     str1.append(ord(char))
#
# for char in word_two_char:
#     str2.append(ord(char))
#
# diff = abs(len(str1) - len(str2))
#
# if len(str1) < len(str2):
#     smallest = len(str1)
# else:
#     smallest = len(str2)
#
# for i in range(0, smallest):
#     suma += str1[i] * str2[i]
#
# if diff > 0:
#     if len(str1) < len(str2):
#         for i in range(len(str1), len(str2)):
#             suma += str2[i]
#     else:
#         for i in range(len(str2), len(str1)):
#             suma += str1[i]
#
# print(suma)









