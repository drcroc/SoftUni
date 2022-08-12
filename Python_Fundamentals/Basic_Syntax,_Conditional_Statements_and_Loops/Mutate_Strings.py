string_one = input()
string_two = input()

word = ''

for i in range(len(string_two)):
    if not string_one[i] == string_two[i]:
        word = string_two[:i+1] + string_one[i+1:]
        print(word)






