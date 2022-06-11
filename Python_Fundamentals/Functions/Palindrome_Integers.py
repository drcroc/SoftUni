def checker(num_list):
    for i in range(0, len(num_list)):
        if num_list[i][::-1] == num_list[i]:
            print(f'True')
        else:
            print(f'False')


num_as_str = input().split(', ')
checker(num_as_str)
