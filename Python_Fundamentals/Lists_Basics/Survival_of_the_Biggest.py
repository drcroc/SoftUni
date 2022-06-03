num_str = str(input())
low_count = int(input())

int_list = list()
str_list = list()
sor = list()
fin = list()

num_list = num_str.split()              # Converting the string into list
for i in range(0, len(num_list)):       # Converting the char in list from string to index
    int_list.append(int(num_list[i]))

sor = int_list.copy()                   # Creating a copy of the int list
int_list.sort(reverse=True)             # Sorting the list in descending order
num_fin = int_list[:-low_count]         # Removing the smallest digits

for i in range(0, len(num_list)):
    if sor[i] in num_fin:               # Comparing the list of the biggest number to the original list
        fin.append(sor[i])              # Entering the bigger numbers in the correct order

for i in range(0, len(fin)):
    str_list.append(str(fin[i]))        # Converting the bigger number list from integer to string

lis = ", ".join(str_list)
print(f'{lis}')                         # Printing the list with ', ' comma and space between the numbers



