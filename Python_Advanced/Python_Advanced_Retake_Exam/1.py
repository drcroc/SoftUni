from collections import deque

caffeine = list(map(int, input().split(', ')))
energy_drinks = deque(map(int, input().split(', ')))

initial = 0

while caffeine and energy_drinks:
    if initial + caffeine[-1] * energy_drinks[0] <= 300:
        initial += caffeine.pop() * energy_drinks.popleft()
    else:
        caffeine.pop()
        energy_drinks.append(energy_drinks.popleft())
        initial -= 30
    if initial < 0:
        initial = 0

if energy_drinks:
    energy_drinks = list(map(str, energy_drinks))
    print(f'Drinks left: {", ".join(energy_drinks)}')
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")

print(f'Stamat is going to sleep with {initial} mg caffeine.')








