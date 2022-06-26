# Add
# Remove
# Replace
# Collapse
# Finish

str_of_num = [int(x) for x in str(input()).split()]

# str_of_num = str(input()).split()
while True:
    command = str(input()).split()
    mem = []
    if command[0] == 'Finish':
        break

    value = int(command[1])

    if command[0] == 'Add':
        str_of_num.append(value)

    elif command[0] == 'Remove':
        if value in str_of_num:
            str_of_num.remove(value)

    elif command[0] == 'Replace':
        if value in str_of_num:
            index = str_of_num.index(value)
            str_of_num.remove(value)
            str_of_num.insert(index, int(command[2]))

    elif command[0] == 'Collapse':
        for i in str_of_num:
            if i >= value:
                mem.append(i)
        str_of_num.clear()
        str_of_num = mem

str_of_num = [str(x) for x in str_of_num]
print(' '.join(str_of_num))

# 1 20 -1 10
# Collapse 8
# Finish

# 5 9 70 -56 9 9
# Replace 9 10
# Remove 9
# Finish

