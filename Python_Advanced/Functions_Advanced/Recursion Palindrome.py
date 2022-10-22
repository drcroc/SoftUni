from collections import deque


def palindrome(*args):
    str_list = deque([x for x in args[0]])
    # for _ in range(len(str_list)//2):
    while len(str_list) > 1:
        if str_list.pop() != str_list.popleft():
            return f'{args[0]} is not a palindrome'

    return f'{args[0]} is a palindrome'


print(palindrome("abcba", 0))
print(palindrome("peter", 0))







