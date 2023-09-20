# Std lib
from abc import ABC, abstractmethod

# Own modules
from player_types.player import Player
from game_collections import Deck


class Boomerang(ABC):
    """
    Abstract class for Boomerang games
    """

    @abstractmethod
    def server_run(self):
        pass

    @abstractmethod
    def client_run():
        pass

    @property
    @abstractmethod
    def _cards_file(self) -> str:
        pass

    def init_server(self, players: list[Player]):
        """
        Initializes the players and states of the game on the server side.
        """
        self.deck = self._get_initialized_deck()

    def _get_initialized_deck(self) -> Deck:
        return Deck(filename=self._cards_file)
