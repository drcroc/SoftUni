
def even_odd(*command):
    odd, even = [], []
    num_list = command[:-1]
    command = command[-1]
    if command == 'even':
        for num in num_list:
            if num % 2 == 0:
                even.append(num)
        return even
    elif command == 'odd':
        for num in num_list:
            if num % 2 != 0:
                odd.append(num)
        return odd













