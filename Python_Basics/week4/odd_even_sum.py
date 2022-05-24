num_c = int(input())
odd = int()
even = int()
for i in range(num_c):
    number = int(input())
    if (i % 2) == 0:
        odd += number
    else:
        even += number

if odd == even:
    print('Yes')
    print('Sum =', odd)
else:
    print('No')
    print('Diff =', abs(odd-even))
