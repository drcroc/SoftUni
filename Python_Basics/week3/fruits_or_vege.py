#     • Плодовете "fruit" имат следните възможни стойности:  banana, apple, kiwi, cherry, lemon и grapes;
#     • Зеленчуците "vegetable" имат следните възможни стойности:  tomato, cucumber, pepper и carrot;

fruit = ['banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes']
vegetable = ['tomato', 'cucumber', 'pepper', 'carrot']

name = str(input())

if name in fruit:
    print('fruit')
elif name in vegetable:
    print('vegetable')
else:
    print('unknown')
