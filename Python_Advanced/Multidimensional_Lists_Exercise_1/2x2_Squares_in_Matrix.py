Rows, Columns = map(int, input().split(' '))
matrix = []
count = 0

for i in range(Rows):
    matrix.append(input().split(' '))

for i in range(Rows-1):
    for j in range(Columns-1):
        if matrix[i][j] == matrix[i][j+1] == matrix[i+1][j] == matrix[i+1][j+1]:
            count += 1

print(count)




