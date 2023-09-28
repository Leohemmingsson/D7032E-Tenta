from player_types import Player
from .deck import Deck


class MultiplePlayers:
    def __init__(self, players: list[Player]) -> None:
        self.players = players

    def broadcast(self, message: str) -> None:
        for player in self.players:
            player.send_message(message)

    def deal_cards(self, deck: Deck, number_of_cards_each: int) -> None:
        """
        Deals one card for each player at a time, until everyone has the given amount of cards.
        """
        for _ in range(number_of_cards_each):
            for player in self.players:
                player.add_card(deck.draw_first_card())
