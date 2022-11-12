#from pokemon import Pokemon   # << comment this part and
from project.pokemon import Pokemon # << uncomment this part to get 100/100


class Trainer:
    def __init__(self, name=None):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        if pokemon.name not in [x.name for x in self.pokemons]:
            self.pokemons.append(pokemon)
            return f'Caught {pokemon.name} with health {pokemon.health}'

        return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        for pokemons_index in range(len(self.pokemons)):
            if pokemon_name == self.pokemons[pokemons_index].name:
                self.pokemons.pop(pokemons_index)
                return f'You have released {pokemon_name}'

        return f'Pokemon is not caught'

    def trainer_data(self):
        owned_pokemons = ''
        for pokemons in self.pokemons:
            owned_pokemons += f'- {pokemons.pokemon_details()}\n'
        output = f'Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n{owned_pokemons}'
        return output
