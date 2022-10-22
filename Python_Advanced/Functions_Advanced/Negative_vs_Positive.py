
num_list = list(map(int, input().split()))


positive = []
negative = []

for nums in num_list:
    if nums > 0:
        positive.append(nums)
    elif nums < 0:
        negative.append(nums)

print(sum(negative))
print(sum(positive))

if abs(sum(negative)) > sum(positive):
    print(f'The negatives are stronger than the positives')
else:
    print(f'The positives are stronger than the negatives')




























