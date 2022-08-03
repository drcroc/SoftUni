unsecured = input()
char_code = []
secured = []

for char in unsecured:
    char_code.append(ord(char) + 3)

for code in char_code:
    secured.append(chr(code))
print(''.join(secured))






