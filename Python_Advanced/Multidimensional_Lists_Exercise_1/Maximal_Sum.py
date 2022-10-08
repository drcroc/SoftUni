Rows, Columns = map(int, input().split(' '))
matrix = []
sub_matrix = []
max_sum = 0

for i in range(Rows):
    matrix.append(list(map(int, input().split(' '))))

for i in range(Rows - 2):
    for j in range(Columns - 2):
        suma = matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] + \
               matrix[i + 1][j] + matrix[i + 1][j + 1] + matrix[i + 1][j + 2] + \
               matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2]

        if suma > max_sum:
            max_sum = suma
            sub_matrix = ([[matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]],
                          [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]],
                          [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]]])

print(f'Sum = {max_sum}')
for x in range(len(sub_matrix)):
    print(' '.join(map(str, sub_matrix[x])))
