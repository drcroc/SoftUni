from project.player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player):
        if any(player.name == x.name for x in self.__players):
            return f'Player {player.name} has already joined'

        self.__players.append(player)
        return f'Player {player.name} joined team {self.__name}'

    def remove_player(self, player_name: str):
        for pos, player in enumerate(self.__players):
            if player.name == player_name:
                del self.__players[pos]
                return player

        return f'Player {player_name} not found'
