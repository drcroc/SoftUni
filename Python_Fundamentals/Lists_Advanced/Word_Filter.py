# Using comprehension, write a program that receives some text,
# separated by space, and take only those words whose length is even.
# Print each word on a new line.

print('\n'.join([word for word in str(input()).split() if len(word) % 2 == 0]))


#   text = str(input()).split()
#   for word in text:
#       if len(word) % 2 == 0:
#           print(word)

