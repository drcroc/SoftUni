import math
people = int(input())
capacity = int(input())


courses = people / capacity
print(f'{math.ceil(courses)}')


