team_A = []
team_B = []
# A-1 A-5 A-10 A-10 B-2 A-7 A-3

cards = str(input())
card_list = cards.split(' ')
terminated = False

for i in range(0, len(card_list)):
    card_team = card_list[i]
    if card_list[i] in team_A or card_list[i] in team_B:
        continue
    if card_team[0] == 'A':
        team_A.append(card_list[i])
    else:
        team_B.append(card_list[i])
    if len(team_A) >= 5 or 5 <= len(team_B):
        terminated = True
        break
if terminated:
    print(f'Team A - {11 - len(team_A)}; Team B - {11 - len(team_B)}')
    print(f'Game was terminated')
else:
    print(f'Team A - {11 - len(team_A)}; Team B - {11 - len(team_B)}')




