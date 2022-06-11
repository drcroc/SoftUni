def sum_numbers(first, second):
    suma = first + second
    return suma


def subtract(suma, third):
    sub = suma - third
    return sub


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(subtract(sum_numbers(first_num, second_num), third_num))


