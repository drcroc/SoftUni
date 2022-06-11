def perfect_num(num):
    suma = 0
    for i in range(1, num):
        if num % i == 0:
            suma += i
    if num == suma:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(perfect_num(number))

