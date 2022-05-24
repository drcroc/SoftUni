brought_food = int(input()) * 1000
food = 0
while True:
    command = input()
    if str(command) == 'Adopted':
        break
    food = food + int(command)

if food <= brought_food:
    food_needed = brought_food - food
    print(f'Food is enough! Leftovers: {abs(food_needed)} grams.')
else:
    food_needed = brought_food - food
    print(f'Food is not enough. You need {abs(food_needed)} grams more.')





