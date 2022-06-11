def even(number):
    if number % 2 == 0:
        return True
    else:
        return False


numbers = str(input()).split(' ')
numbers = [int(i) for i in numbers]

only_evens = list(filter(even, numbers))
print(only_evens)
