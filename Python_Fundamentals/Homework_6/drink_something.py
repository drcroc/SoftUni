age = int(input())
if 14 < age <= 18:
    print(f'drink coke')    # teen
elif 18 < age <= 21:
    print(f'drink beer')    # young adult
elif age > 21:
    print(f'drink whisky')  # adult
else:
    print(f'drink toddy')

# A kid is defined as someone under or at the age of 14.
# A teen is defined as someone under or at the age of 18.
# A young adult is defined as someone under or at the age of 21.
# An adult is defined as someone above the age of 21.
# Note: All the values are inclusive except the last one!

