def even(number):
    if number % 2 == 0:
        return True

    return False


numbers = str(input()).split(' ')
numbers = [int(i) for i in numbers]

only_evens = filter(even, numbers)
evens = list(only_evens)
print(evens)
