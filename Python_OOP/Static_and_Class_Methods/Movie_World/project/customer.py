class Customer:
    def __init__(self, name: str, age: int, id: int):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []

    def __repr__(self):
        film_list = [film.name for film in self.rented_dvds]

        return f'{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)}' \
               f' rented DVD\'s ({", ".join(film_list)})'


