# Using a list comprehension, write a program that receives numbers,
# separated by comma and space ", ", and prints all the positive, negative,
# even, and odd numbers on separate lines as shown below.
# Note: Zero is counted for a positive number

positive = []
negative = []
even = []
odd = []

list_int = [int(i) for i in input().split(', ')]

for i in list_int:
    if i >= 0:
        positive.append(str(i))
        if i % 2 == 0:
            even.append(str(i))
        else:
            odd.append(str(i))
    else:
        negative.append(str(i))
        if i % 2 == 0:
            even.append(str(i))
        else:
            odd.append(str(i))

print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")
















