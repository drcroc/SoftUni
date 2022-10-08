set_one = set(map(int, input().split()))
set_two = set(map(int, input().split()))

Lines = int(input())

for _ in range(Lines):
    command = input()

    if 'Add First' in command:
        [set_one.add(int(x)) for x in command.split() if x.isdigit()]

    elif 'Add Second' in command:
        [set_two.add(int(x)) for x in command.split() if x.isdigit()]

    elif 'Remove First' in command:
        [set_one.discard(int(x)) for x in command.split() if x.isdigit()]

    elif 'Remove Second' in command:
        [set_two.discard(int(x)) for x in command.split() if x.isdigit()]

    else:
        if set_two.issubset(set_one) or set_one.issubset(set_two):
            print('True')
        else:
            print('False')

print(*set_one, sep=', ')
print(*set_two, sep=', ')
