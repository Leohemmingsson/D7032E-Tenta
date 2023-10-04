# std
from typing import final
import asyncio

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
            self._reset_round()
        input()

    def _start_rount(self) -> None:
        self.players.deal_cards(self.deck, 7)
        for _ in range(7):
            self.players.show_each_player_their_cards()
            asyncio.run(self.players.choose_cards())

    def _count_score(self) -> None:
        raise NotImplementedError(f"Method not implemented for {type(self).__name__}")

    def _reset_round(self) -> None:
        cards_from_players = self.players.get_all_cards()
        cards_from_players.shuffle()
        self.deck.add_deck(cards_from_players)
