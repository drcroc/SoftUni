import re

# pattern = r'(www|(?<=\s))[.]([a-zA-Z0-9]+[-]?[a-zA-Z0-9]+)([.][a-z]+)+' 80/100
pattern = r'www.([a-zA-Z0-9\-]+)(\.[a-z]+)+'

while True:
    text = input()
    if text:
        result = re.finditer(pattern, text)
        for show in result:
            print(show[0])
    else:
        break



