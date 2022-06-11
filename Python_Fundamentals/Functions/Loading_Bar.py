def loader(load_num):
    if load_num == 100:
        print(f'{load_num}% Complete!\n[%%%%%%%%%%]')
    else:
        num = load_num // 10
        print(f'{load_num}% [{num * "%"}{(10 - num) * "."}]\nStill loading...')


load = int(input())
loader(load)
