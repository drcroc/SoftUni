# Вход
# От конзолата се четат:
#  На първия ред – N – броят дни – цяло число в интервала [1...300]
#  За всеки един ден на отделен ред:
#  количество на ракията – реално число в интервала [1.00...500.00]
#  градус на получената напитка - реално число в интервала [10.00...99.00]
# Изход
# Да се отпечатат на конзолата 3 реда:
#  Първи ред: "Liter: {общо литрите}"
#  Втори ред: "Degrees: {градусите на общата смес}"
#  Трети ред – да се отпечатва един от следните редове:

#  "Not good, you should baking!" - ако градусът е по-малък от 38
#  "Super!" - ако градусът е от 38 до 42
#  "Dilution with distilled water!" - aко градусът е по-голям от 42
degrees = 0.00
liter = 0.00
day = int(input())
for i in range(0, day):
    liter_inp = float(input())
    degrees_inp = float(input())
    liter = liter + liter_inp
    degrees = degrees + degrees_inp * liter_inp

avg_degree = degrees / liter
print(f'Liter: {liter:.2f}')
print(f'Degrees: {avg_degree:.2f}')
if avg_degree > 42:
    print(f'Dilution with distilled water!')
elif 38 < avg_degree < 42:
    print(f'Super!')
else:
    print(f'Not good, you should baking!')
