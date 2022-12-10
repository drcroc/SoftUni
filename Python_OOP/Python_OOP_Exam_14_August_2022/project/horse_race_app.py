from project.jockey import Jockey
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.horse_race import HorseRace


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    @property
    def horse_type(self):
        return {
            "Appaloosa": Appaloosa,
            "Thoroughbred": Thoroughbred
        }

    def __find_horse(self, h_type):
        return [h for h in self.horses if h.__class__.__name__ == h_type][-1]

    def __find_jockey(self, jockey_name: str):
        for j in self.jockeys:
            if j.name == jockey_name:
                return j

    def __find_race(self, type_race: str):
        for r in self.horse_races:
            if r.race_type == type_race:
                return r

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if any(horse_name == h.name for h in self.horses):
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.horse_type:
            self.horses.append(self.horse_type[horse_type](horse_name, horse_speed))
            return f'{horse_type} horse {horse_name} is added.'

    def add_jockey(self, jockey_name: str, age: int):
        if any(jockey_name == j.name for j in self.jockeys):
            raise Exception(f"Jockey {jockey_name} has been already added")

        self.jockeys.append(Jockey(jockey_name, age))
        return f'Jockey {jockey_name} is added.'

    def create_horse_race(self, race_type: str):
        if any(race_type == r.name for r in self.horse_races):
            raise Exception(f"Race {race_type} has been already created!")

        self.horse_races.append(HorseRace(race_type))
        return f'Race {race_type} is created.'

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        if not self.__find_jockey(jockey_name):
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not self.__find_horse(horse_type) or self.__find_horse(horse_type).is_taken:
            raise Exception(f'Horse breed {horse_type} could not be found!')

        horse = self.__find_horse(horse_type)
        jockey = self.__find_jockey(jockey_name)

        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        horse.is_taken = True
        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        if not self.__find_jockey(jockey_name):
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not self.__find_race(race_type):
            raise Exception(f"Race {race_type} could not be found!")

        race = self.__find_race(race_type)
        jockey = self.__find_jockey(jockey_name)

        if jockey.horse is None:
            return f"Jockey {jockey_name} cannot race without a horse!"

        if any(jockey_name == j.name for j in race.jockeys):
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        if not self.__find_race(race_type):
            raise Exception(f"Race {race_type} could not be found!")

        race = self.__find_race(race_type)

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = sorted(race.jockeys, key=lambda x: -x.horse.speed)[0]

        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h " \
               f"is {winner.name}! Winner's horse: {winner.horse.name}."





