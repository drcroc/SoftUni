numbers_dictionary = {}

line = input()

while line != "Search":
    try:
        number_as_string = line
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print('The variable number must be an integer')
    line = input()


line = input()
while line != "Remove":
    try:
        searched = line
        print(numbers_dictionary[searched])
    except KeyError:
        print(f'Number does not exist in dictionary')
    line = input()


line = input()
while line != "End":
    try:
        searched = line
        del numbers_dictionary[searched]
    except KeyError:
        print(f'Number does not exist in dictionary')

    line = input()

print(numbers_dictionary)


# one
# two
# Search
# Remove
# End

# one
# 1
# two
# 2
# Search
# one
# Remove
# two
# End

# one
# 1
# Search
# one
# Remove
# two
# End

























