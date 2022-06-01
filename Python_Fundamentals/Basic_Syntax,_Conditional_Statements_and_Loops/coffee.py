word = str()
coffee = int()

while True:
    word = str(input())
    if word == 'END' or word == 'end':
        break
    if word == 'dog' or word == 'cat' or word == 'coding' or word == 'movie':
        coffee += 1
    elif word == 'DOG' or word == 'CAT' or word == 'CODING' or word == 'MOVIE':
        coffee += 2
    else:
        continue

if coffee > 5:
    print(f'You need extra sleep')
else:
    print(f'{coffee}')


