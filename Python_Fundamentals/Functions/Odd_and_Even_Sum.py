def even_odd(num, even=0, odd=0):
    for i in range(0, len(num)):
        if int(num[i]) % 2 == 0:
            even += int(num[i])
        else:
            odd += int(num[i])

    print(f"Odd sum = {odd}, Even sum = {even}")


even_odd(str(input()))
