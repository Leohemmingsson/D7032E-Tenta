# Std lib
from abc import ABC, abstractmethod

# Own modules
from player_types.Player import Player
from game_collections import Deck


class Boomerang(ABC):
    """
    Abstract class for Boomerang games

    Args:
        players (list[Player]): List of players in the game

    """

    def __init__(self, players: list[Player]):
        self.deck = self._get_initialized_deck()

    @abstractmethod
    def _get_initialized_deck(self) -> Deck:
        pass
