def min_num(num_list):
    return min(num_list)


def max_num(num_list):
    return max(num_list)


def sum_list(num_list):
    suma = 0
    for i in num_list:
        suma += i
    return suma


num_as_str = input().split()
num_as_int = [int(i) for i in num_as_str]

print(f'The minimum number is {min_num(num_as_int)}')
print(f'The maximum number is {max_num(num_as_int)}')
print(f'The sum number is: {sum_list(num_as_int)}')

