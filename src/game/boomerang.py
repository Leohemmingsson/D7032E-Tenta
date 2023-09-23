# Own modules
from player_types.player import Player
from game_collections import Deck


class Boomerang:
    def __init__(self, players: list[Player], deck: Deck) -> None:
        self.players = players
        self.deck = deck

    def start_game(self) -> None:
        print("Starting game")
