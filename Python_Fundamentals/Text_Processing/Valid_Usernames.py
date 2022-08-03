password_list = input().split(', ')

for password in password_list:
    pass_valid = True

    for pass_char in password:
        if pass_char.isspace():
            pass_valid = False
            break

        if pass_char.isalpha() or pass_char.isdigit() or pass_char in '-_':
            pass_valid = True
        else:
            pass_valid = False
            break

    if not 3 <= len(password) <= 16:
        pass_valid = False

    if pass_valid:
        print(password)


