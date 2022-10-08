colors = []
randomized = input().split()
main_color = ["red", "yellow", "blue", "orange", "purple", "green"]
color_reversed, first_str, second_str = '', '', ''

while randomized:
    if len(randomized) > 1:
        first_str, second_str = randomized.pop(0), randomized.pop(-1)

        for color in (first_str + second_str, second_str + first_str):
            if color in main_color:
                colors.append(color)

        else:
            first_str, second_str = first_str[:-1], second_str[:-1]

            if first_str:
                randomized.insert(len(randomized) // 2, first_str)
            if second_str:
                randomized.insert(len(randomized) // 2, second_str)
    else:
        color = randomized.pop(0)
        if color in main_color:
            colors.append(color)

if 'orange' in colors:
    if 'yellow' not in colors or 'red' not in colors:
        colors.remove('orange')

if 'purple' in colors:
    if 'red' not in colors or 'blue' not in colors:
        colors.remove('purple')

if 'green' in colors:
    if 'yellow' not in colors or 'blue' not in colors:
        colors.remove('green')

print(colors)
