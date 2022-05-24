#   Град    # 0 ≤ s ≤ 500   # 500 < s ≤ 1 000   # 1 000 < s ≤ 10 000    # s > 10 000
# Sofia     # 5%            # 7%                # 8%                    # 12%
# Varna     # 4.5%          # 7.5%              # 10%                   # 13%
# Plovdiv   # 5.5%          # 8%                # 12%                   # 14.5%

sofia_com = [5, 7, 8, 12]
varna_com = [4.5, 7.5, 10, 13]
plovdiv_com = [5.5, 8, 12, 14.5]
city_list = ['Sofia', 'Varna', 'Plovdiv']
city = str(input())
sells = float(input())
commission = 0
if city not in city_list:
    print('error')
    exit()
if 0 <= sells <= 500:
    if city == 'Sofia':
        commission = (sofia_com[0] / 100) * sells
    # print(f'{commission:.2f}')
    elif city == 'Varna':
        commission = (varna_com[0] / 100) * sells
    # print(f'{commission:.2f}')
    elif city == 'Plovdiv':
        commission = (plovdiv_com[0] / 100) * sells
    # print(f'{commission:.2f}')
    else:
        print('error')
    print(f'{commission:.2f}')
elif 500 < sells <= 1000:
    if city == 'Sofia':
        commission = (sofia_com[1] / 100) * sells
    elif city == 'Varna':
        commission = (varna_com[1] / 100) * sells
    elif city == 'Plovdiv':
        commission = (plovdiv_com[1] / 100) * sells
    else:
        print('error')
    print(f'{commission:.2f}')
elif 1000 < sells <= 10000:
    if city == 'Sofia':
        commission = (sofia_com[2] / 100) * sells
    elif city == 'Varna':
        commission = (varna_com[2] / 100) * sells
    elif city == 'Plovdiv':
        commission = (plovdiv_com[2] / 100) * sells
    else:
        print('error')
    print(f'{commission:.2f}')
elif sells > 10000:
    if city == 'Sofia':
        commission = (sofia_com[3] / 100) * sells
    elif city == 'Varna':
        commission = (varna_com[3] / 100) * sells
    elif city == 'Plovdiv':
        commission = (plovdiv_com[3] / 100) * sells
    else:
        print('error')
    print(f'{commission:.2f}')
else:
    print('error')
