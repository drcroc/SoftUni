# Chat =  Add the message at the last position in the chat
# Delete =  Delete the message if it exists or ignore command
# Edit =  Update the message with edited version or ignore command
# Pin =  Find the given message and move it to the last index or ignore command
# Spam =  Add all messages at the en    d of the chat
# end =  Stop receiving commands , print the log
chat = []

while True:
    command = str(input()).split()

    if command[0] == 'end':
        break

    message = command[1]

    if command[0] == 'Chat':
        chat.append(message)

    elif command[0] == 'Delete':
        if message in chat:
            chat.remove(message)
        else:
            pass

    elif command[0] == 'Edit':
        if message in chat:
            index = chat.index(message)
            chat.remove(message)
            chat.insert(index, (command[2]))
        else:
            pass

    elif command[0] == 'Pin':
        if message in chat:
            chat.append(message)
            chat.remove(message)
        pass

    elif command[0] == 'Spam':
        for i in range(1, len(command)):
            chat.append(command[i])
        pass

print('\n'.join(chat))


# [command[0] message[1] message[2] message[3] message[n]]











