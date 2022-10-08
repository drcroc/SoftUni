Lines = int(input())
matrix = []
prime_diagonal, second_diagonal = [], []

for i in range(Lines):
    matrix.append(list(map(int, input().split(' '))))
    prime_diagonal.append(matrix[i][i])
    second_diagonal.append(matrix[i][-1-i])

print(f'{abs(sum(prime_diagonal) - sum(second_diagonal))}')
