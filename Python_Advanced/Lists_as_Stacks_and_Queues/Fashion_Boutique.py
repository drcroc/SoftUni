
stack = input().split()
racks_capacity = int(input())

racks_count = 1     # Count of racks that have been used
current_rack = 0    # Value of the clothes at rack

while stack:
    clothe_value = int(stack.pop())
    if current_rack + clothe_value <= racks_capacity:
        current_rack += clothe_value

    else:
        racks_count += 1
        current_rack = clothe_value

print(racks_count)












