# std
from typing import final

# Own modules
from game_collections import Deck, MultiplePlayers


class Boomerang:
    def __init__(self, players: MultiplePlayers, deck: Deck) -> None:
        self.players = players
        self.deck = deck

    @final
    def start_game(self) -> None:
        """
        This is the game loop, this should be the same for all boomering games.

        If anything is different in a extension, that part should be moved to separate methods.
        """

        self.players.broadcast("Starting game")
        for _ in range(4):
            self._start_rount()
            self._count_score()
        input()

    def _start_rount(self) -> None:
        self.players.deal_cards(self.deck, 7)
        self.players.show_all_player_stats()
        self._throw_card()
        ...

    def _throw_card(self) -> None:
        self.players.broadcast("")

    def _count_score(self) -> None:
        print("default")
