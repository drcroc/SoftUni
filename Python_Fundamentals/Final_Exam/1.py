
text = input().split()

while True:

    commands = input()

    if commands == 'Done':
        break

    commands = commands.split(' ')

    if commands[0] == 'Change':  # Replace
        for i, name in enumerate(text):
            if commands[1] in name:
                index = text[i].index(commands[1])
                text[i] = text[i][:index] + commands[2] + text[i][index + 1:]
        print(' '.join(text))

    elif commands[0] == 'Includes':  # Include
        if commands[1] in ' '.join(text):
            print('True')
        else:
            print('False')

    elif commands[0] == 'End':  # End
        if ' '.join(text).endswith(commands[1]):
            print('True')
        else:
            print('False')

    elif commands[0] == 'FindIndex':  # FindIndex
        index = ' '.join(text).index(commands[1])
        print(index)

    elif commands[0] == 'Cut':  # Cut
        text = ' '.join(text)
        start_index, count = int(commands[1]), int(commands[2])
        text = text[start_index: start_index+count]
        print(text)

    else:  # Uppercase
        text = [txt.upper() for txt in text]
        print(' '.join(text))









