import re

date = input()

pattern = r'([0-9]{2})([-.\/])([A-Z][a-z]+)\2([0-9]{4})'


for x in re.findall(pattern, date):
    print(f'Day: {x[0]}, Month: {x[2]}, Year: {x[3]}')
