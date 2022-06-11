def pass_len(string):
    if len(string) > 10 or 6 > len(string):
        print(f'Password must be between 6 and 10 characters')
        return True


def no_special_chr(string):
    for i in range(0, len(string)):
        if not string[i].isalpha():
            if not string[i].isnumeric():
                print(f'Password must consist only of letters and digits')
                return True


def more_digits(string):
    digits = 0
    for i in range(0, len(string)):
        if string[i].isdigit():
            digits += 1

    if digits < 2:
        print(f'Password must have at least 2 digits')
        return True


def pass_checker(string):
    valid = True
    if pass_len(string):
        valid = False
    if no_special_chr(string):
        valid = False
    if more_digits(string):
        valid = False
    if valid:
        print('Password is valid')


char = input()
pass_checker(char)
