str_chars = input()

print(str_chars[0], end='')
for i in range(1, len(str_chars)):

    if str_chars[i] != str_chars[i-1]:
        print(f'{str_chars[i]}', end='')



