
text = str(input())
lowercase = text.lower()

a_count = 0
i_count = 0
u_count = 0
e_count = 0
o_count = 0
for vowel in "a":
    a_count = lowercase.count(vowel)
for vowel in "i":
    i_count = lowercase.count(vowel)
for vowel in "o":
    o_count = lowercase.count(vowel)
for vowel in "e":
    e_count = lowercase.count(vowel)
for vowel in "u":
    u_count = lowercase.count(vowel)

x = a_count*1 + e_count*2 + i_count*3 + u_count*5 + o_count*4
print(x)
# # a     1
# # e     2
# # i     3
# # o     4
# # u     5
#
# text = str(input())
# x = 0
# a = 1
# e = 2
# i = 3
# o = 4
# u = 5
#
# for i in "aeiou":
#     count = text.count(i)
# print(count)