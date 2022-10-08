n_lines = int(input())
stack = []

for _ in range(n_lines):
    command = input().split()
    if len(command) > 1:
        num = int(command[-1])
        command = command[0]

    if command == '1':
        stack.append(num)
    elif '2' in command and stack:
        stack.pop()
    elif '3' in command and stack:
        print(max(stack))
    # elif '4' in command:
    else:
        if stack:
            print(min(stack))

stack.reverse()
print(', '.join(map(str, stack)))





