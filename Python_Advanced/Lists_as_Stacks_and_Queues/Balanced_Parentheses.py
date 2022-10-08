sequence = input()
stack = []
result = True

for char in range(len(sequence)):
    if sequence[char] in ['(', '[', '{']:
        stack.append(sequence[char])

    elif sequence[char] == ')':
        if stack and stack[-1] == '(':
            stack.pop()
        else:
            result = False
            break
    elif sequence[char] == ']':
        if stack and stack[-1] == '[':
            stack.pop()
        else:
            result = False
            break
    elif stack and sequence[char] == '}':
        if stack[-1] == '{':
            stack.pop()
        else:
            result = False
            break
    else:
        result = False
        break

if result:
    print(f'YES')
else:
    print(f'NO')
