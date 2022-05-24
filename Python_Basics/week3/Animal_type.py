# Напишете програма, която отпечатва класа на животното според неговото име, въведено от потребителя.
#     1. dog -> mammal
#     2. crocodile, tortoise, snake -> reptile
#     3. others -> unknown

animal_type = str(input())

mammal = ['dog']
reptile = ['crocodile', 'tortoise', 'snake']

if animal_type in mammal:
    print('mammal')
elif animal_type in reptile:
    print('reptile')
else:
    print('unknown')
