Rows, Columns = map(int, input().split(' '))
matrix = []

for i in range(Rows):
    matrix.append([])
    for j in range(Columns):
        matrix[i].append(f'{chr(97+i)}{chr(97+i+j)}{chr(97+i)}')

    print(' '.join(matrix[i]))
