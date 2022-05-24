# Трима спортни състезатели финишират за някакъв брой секунди (между 1 и 50).
# Да се напише програма, която чете времената на състезателите в секунди,
# въведени от потребителя и пресмята сумарното им време във формат "минути:секунди".
# Секундите да се изведат с водеща нула (2  "02", 7  "07", 35  "35").

first_person = int(input())
second_person = int(input())
third_person = int(input())

seconds = first_person + second_person + third_person

minutes = seconds // 60
second_seconds = seconds-minutes*60

if second_seconds < 9:
    print(f'{minutes}:0{second_seconds}')
else:
    print(f'{minutes}:{second_seconds}')
