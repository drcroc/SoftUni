Lines = int(input())
matrix = []
prime_diagonal, second_diagonal = [], []

for i in range(Lines):
    matrix.append(list(map(int, input().split(', '))))
    prime_diagonal.append(matrix[i][i])
    second_diagonal.append(matrix[i][-1-i])

print(f"Primary diagonal: {', '.join(map(str, prime_diagonal))}. Sum: {sum(prime_diagonal)}")
print(f"Secondary diagonal: {', '.join(map(str, second_diagonal))}. Sum: {sum(second_diagonal)}")
