from abc import ABC

from game_collections import Deck


class Player(ABC):
    def __init__(self, hand: Deck) -> None:
        self.hand = hand
