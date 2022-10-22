from os import linesep

Weather = {
    "Sunny": '1',
    'Cloudy': '2',
    "Rainy": '3'}


def forecast(*args):
    output = []
    weather_loc = {}
    for loc, weather in args:
        if Weather[weather] not in weather_loc.keys():
            weather_loc[Weather[weather]] = []
        weather_loc[Weather[weather]].append(loc)
    for key, items in sorted(weather_loc.items()):
        weather = (list(Weather.keys())[list(Weather.values()).index(key)])
        for city in sorted(items):
            output.append(f'{city} - {weather}')
    return linesep.join(output)

