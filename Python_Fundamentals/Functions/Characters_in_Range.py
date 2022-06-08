def chr_to(first_chr, second_chr):
    first_ascii = ord(first_chr)
    second_ascii = ord(second_chr)
    for i in range(int(first_ascii) + 1, int(second_ascii)):
        print(f'{chr(i)}', end=' ')


chr_to(input(), input())

