
chars = str(input())
count = int(input())

chars_first = list()
chars_second = list()
chars_list = chars.split()  # Splitting the char string into the list
half_point = len(chars_list)//2

for _ in range(0, count):

    chars_first = chars_list[:half_point]
    chars_second = chars_list[half_point:]
    chars_list.clear()
    for i in range(0, half_point):
       chars_list.append(chars_first[i])
       chars_list.append(chars_second[i])
    chars_first.clear()
    chars_second.clear()

print(f'{chars_list}')
