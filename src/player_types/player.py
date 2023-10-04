import socket

from data_structures import ClientConnectionInfo, Card
from game_collections import Deck


class Player:
    def __init__(self) -> None:
        self._score = 0
        self.hand = Deck()
        self._chosen_card = Deck()

    def send_message(self, message: str) -> None:
        raise NotImplementedError(f"Method not implemented for {type(self).__name__}")

    def show_cards_in_hand(self) -> None:
        raise NotImplementedError(f"Method not implemented for {type(self).__name__}")

    def choose_card(self) -> None:
        raise NotImplementedError(f"Method not implemented for {type(self).__name__}")

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @property
    def socket_obj(self) -> socket.socket:
        return self._socket

    @socket_obj.setter
    def socket_obj(self, value: socket.socket) -> None:
        self._socket = value

    @property
    def score(self) -> int:
        return self._score

    @property
    def cards_in_hand(self) -> Deck:
        return self.hand

    @property
    def chosen_cards(self) -> Deck:
        """
        Returns all cards that the player has chosen, exept the throw card. (The first card in the deck)
        """
        new_deck = Deck(list(self._chosen_card)[1:])
        return new_deck

    @property
    def all_chosen_cards(self) -> Deck:
        """
        Returns all cards that the player has chosen, including the throw card.
        """
        return self._chosen_card

    def add_score(self, value: int) -> None:
        self._score += value

    def add_card_to_hand(self, card: Card) -> None:
        self.hand.add_card(card)

    def _choose_card_from_site(self, site: str) -> None:
        """
        Takes chosen card from hand and places in chosen cards.
        """
        card = self.hand.pick_from_site(site)
        self._chosen_card.add_card(card)

    def _choose_first_card(self) -> None:
        card = self.hand.draw_first_card()
        self._chosen_card.add_card(card)

    def get_all_cards(self) -> Deck:
        """
        Returns all cards that a player has, in hand and chosen cards.
        The player will not have any cards in hand or as chosen.
        """

        all_cards = Deck()
        all_cards.add_deck(self.hand)
        all_cards.add_deck(self._chosen_card)
        self.hand = Deck()
        self._chosen_card = Deck()
        return all_cards

    @classmethod
    def from_client_connection_info(cls, connection_info: ClientConnectionInfo) -> "Player":
        c = cls()
        c.id = connection_info.id
        c.socket_obj = connection_info.socket_connection
        return c

    @classmethod
    def from_id(cls, id: int) -> "Player":
        c = cls()
        c.id = id
        return c
