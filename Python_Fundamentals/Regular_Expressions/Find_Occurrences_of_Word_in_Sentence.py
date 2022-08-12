import re

sentence = input().lower()
word = input().lower()

pattern = r'\b' + word + r'\b'

# print(len(list(re.finditer(pattern, sentence))))
match = re.finditer(pattern, sentence)
