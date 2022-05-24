# Да се напише програма, която чете час и минути от 24-часово денонощие,
# въведени от потребителя и изчислява колко ще е часът след 15 минути.
# Резултатът да се отпечата във формат часове:минути.
# Часовете винаги са между 0 и 23, а минутите винаги са между 0 и 59.
# Часовете се изписват с една или две цифри.
# Минутите се изписват винаги с по две цифри, с водеща нула, когато е необходимо.


hours = int(input())
minutes = int(input())

new_minutes = minutes + 15 + hours * 60
new_hours = new_minutes // 60
final_minutes = new_minutes - new_hours * 60

if new_hours > 23:
    new_hours = 0

if final_minutes < 9:
    print(f'{new_hours}:0{final_minutes}')
else:
    print(f'{new_hours}:{final_minutes}')





