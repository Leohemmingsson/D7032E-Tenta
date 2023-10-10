# std
from typing import final

# Own modules
from game_collections import Deck, MultiplePlayers


class Boomerang:
    def __init__(self, players: MultiplePlayers, deck: Deck) -> None:
        self.players = players
        self.deck = deck
        self._set_constants()
        self._make_sure_all_constants_are_set()

    @final
    def start_game(self) -> None:
        """
        This is the game loop, this should be the same for all boomering games.

        If anything is different in a extension, that part should be moved to separate methods.
        """

        self.players.broadcast("Starting game")
        for _ in range(self._NR_OF_ROUNDS):
            self._start_round()
            self._count_score_after_round()
            self._reset_round()
        self._count_score_after_game()
        input()

    def _start_round(self) -> None:
        self.players.deal_cards(self.deck, self._CARDS_IN_HAND)
        for _ in range(self._CARDS_IN_HAND):
            self.players.show_each_player_their_cards()
            self.players.choose_cards()
            self.players.rotate_cards_in_hand()
            # self.players.clear_screen()

            self.players.show_all_players_draft()
            self.players.broadcast("-----------------------------------")
            self._count_score_after_draft()

    def _count_score_after_round(self) -> None:
        """
        This is triggered after each round. (When all players have played all their cards)
        """
        ...

    def _count_score_after_draft(self) -> None:
        """
        This is triggered after each player has drafted a card.
        """
        ...

    def _count_score_after_game(self) -> None:
        """
        This is only triggered once, when all rounds are over.
        """
        ...

    def _set_constants(self) -> None:
        raise NotImplementedError(f"Method not implemented for {type(self).__name__}")

    def _reset_round(self) -> None:
        cards_from_players = self.players.get_all_cards()
        cards_from_players.shuffle()
        self.deck.add_deck(cards_from_players)

    def _make_sure_all_constants_are_set(self):
        if "_NR_OF_ROUNDS" not in self.__dict__:
            raise ValueError("NR_OF_ROUNDS is not set.")

        if "_CARDS_IN_HAND" not in self.__dict__:
            raise ValueError("CARDS_IN_HAND is not set.")
