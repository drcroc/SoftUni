def even_odd_filter(**command):
    odd, even = [], []

    for keys in command.keys():
        if keys == 'even':
            for num in command[keys]:
                if num % 2 == 0:
                    even.append(num)
                    # command[keys].remove(num)
            command[keys] = even

        elif keys == 'odd':
            for num in command[keys]:
                if num % 2 != 0:
                    odd.append(num)
            command[keys] = odd

    return dict(sorted(command.items()))
