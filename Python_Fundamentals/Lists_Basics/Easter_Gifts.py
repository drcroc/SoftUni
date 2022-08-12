products = input().split()

while True:
    command = input()
    if command == 'No Money':
        break
    command = command.split()

    # if command[0] == 'OutOfStock':
    #     while True:
    #         if command[1] in products:
    #             products.remove(command[1])
    #         else:
    #             break
    if "OutOfStock" in command[0]:
        for i, name in enumerate(products):
            if command[1] == name:
                products[i] = "None"

    # elif "Required" in command[0]:
    #     length = len(products)
    #     if length > int(command[2]) >= 0:
    #         products[int(command[2])] = command[1]
    # elif "JustInCase" in command[0]:
    #     products[-1] = command[1]

    elif command[0] == 'Required':
        if len(products) > int(command[2]) > 0:
            products[int(command[2])] = command[1]

    elif command[0] == 'JustInCase':
        products[-1] = command[1]
print(" ".join(x for x in products if x != "None"))

