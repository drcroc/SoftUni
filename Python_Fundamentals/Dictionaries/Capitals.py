# Using a dictionary comprehension,
# write a program that receives country names on the first line, separated by comma and space ", ",
# and their corresponding capital cities on the second line
# (again separated by comma and space ", ").
# Print each country with their capital on a separate line in the following format: "{country} -> {capital}".

# country_city = dict()
country_list = str(input()).split(', ')
city_list = str(input()).split(', ')

country_city = {country_list[i]: city_list[i] for i in range(len(country_list))}
# for i in range(0, len(country_list)):
#   country_city[country_list[i]] = city_list[i]

for country, capital in country_city.items():
    print(f'{country} -> {capital}')
