# Own modules
from game_collections import Deck, MultiplePlayers


class Boomerang:
    def __init__(self, players: MultiplePlayers, deck: Deck) -> None:
        self.players = players
        self.deck = deck

    def start_game(self) -> None:
        self.players.broadcast("Starting game")
        input()
