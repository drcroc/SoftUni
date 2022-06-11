#    Write a function that receives two integer numbers. Calculate the factorial of each number.
#    Divide the first result by the second and print the division formatted to the second decimal point.


def calc(num_1):
    for i in range(1, num_1):
        num_1 *= i
    return num_1


int1 = int(input())
int2 = int(input())

print(f'{calc(int1)/calc(int2):.2f}')
