import math
divisor = int(input())
boundary = int(input())

privately = math.floor(boundary / divisor)
largest_int = privately * divisor
print(f'{largest_int}')

