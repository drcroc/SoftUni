string = str()

loop = True
while loop:
    double_str = str()
    string = str(input())
    if string == 'SoftUni':
        continue
    if string == 'End':
        break

    for i in range(len(string)):
        double_str = double_str + (string[i] + string[i])

    print(f'{double_str}')
    # Double_str=






