
import re

main_string = input()

pattern = r"(^|(?<=\s))([A-Za-z0-9])+([\.\_\-][a-zA-Z0-9]+)*@([a-zA-Z-]+)\.([a-zA-Z-]+)([\.A-Za-z-])*(\b|(?=\s))"
result = re.finditer(pattern, main_string)
for show in result:
    print(show[0])

#


# (^|(?<=\s))([A-Za-z0-9])+([\.\_\-][a-zA-Z0-9]+)*@([a-zA-Z]+)\.([a-zA-Z]+)([\.A-Za-z-])*(\b|(?=\s))
#r"(^|(?<=\s))([A-Za-z0-9])+([\.\-\_][A-Za-z0-9]+)*@([A-Za-z-]+)\.([A-Za-z-]+)([\.A-Za-z-])*(\b|(?=\s))")
#              (([a-zA-Z0-9._-]+)@([a-zA-Z]+)\.([a-zA-Z]+))([\.A-Za-z-])