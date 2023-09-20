from abc import ABC, abstractmethod

from game_collections import Deck


class Player(ABC):
    def __init__(self, hand: Deck) -> None:
        self.hand = hand
        self.score = 0

    @abstractmethod
    def send_message(self, message: str) -> None:
        pass
