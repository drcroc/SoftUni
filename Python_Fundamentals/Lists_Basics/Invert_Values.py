# Write a program that receives a single string containing positive and negative numbers separated by a single space.
# Print a list containing the opposite of each number.

numbers = str(input())
number = numbers.split()
for i in range(0, len(number)):
    number[i] = int(number[i]) * -1

print(f'{number}')





