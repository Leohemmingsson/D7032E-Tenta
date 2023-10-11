import socket

from data_structures import ClientConnectionInfo, Card, Map
from game_collections import Deck


class Player:
    def __init__(self, id: int, map: Map) -> None:
        self._id = id
        self._map = map
        self._score = 0
        self._hand = Deck()
        self._chosen_card = Deck()

    def send_message(self, message: str) -> None:
        raise NotImplementedError(f"Method not implemented for {type(self).__name__}")

    def show_cards_in_hand(self) -> None:
        raise NotImplementedError(f"Method not implemented for {type(self).__name__}")

    def choose_card(self) -> None:
        raise NotImplementedError(f"Method not implemented for {type(self).__name__}")

    def clear_screen(self) -> None:
        raise NotImplementedError(f"Method not implemented for {type(self).__name__}")

    @property
    def id(self) -> int:
        return self._id

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
        return self._hand

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

    def get_completed_regions_not_taken(self, taken: list[str]) -> list[str]:
        return self._map.get_completed_regions_not_taken(taken)

    def add_score(self, value: int) -> None:
        self._score += value

    def add_card_to_hand(self, card: Card) -> None:
        self._hand.add_card(card)

    def add_deck_to_hand(self, deck: Deck) -> None:
        self._hand.add_deck(deck)

    def get_all_cards(self) -> Deck:
        """
        Returns all cards that a player has, in hand and chosen cards.
        The player will not have any cards in hand or as chosen.
        """

        all_cards = Deck()
        all_cards.add_deck(self._hand)
        all_cards.add_deck(self._chosen_card)
        self._hand = Deck()
        self._chosen_card = Deck()
        return all_cards

    def get_all_cards_in_hand(self) -> Deck:
        hand = self._hand
        self._hand = Deck()
        return hand

    def _choose_card_from_site(self, site: str) -> None:
        """
        Takes chosen card from hand and places in chosen cards.
        """
        self._map.visit_place(site)
        card = self._hand.pick_from_site(site)
        self._chosen_card.add_card(card)

    def _choose_first_card(self) -> None:
        card = self._hand.draw_first_card()
        self._chosen_card.add_card(card)

    @classmethod
    def from_client_connection_info(cls, connection_info: ClientConnectionInfo, map: Map) -> "Player":
        """
        Construct a person using ClientConnectionInfo
        """
        c = cls(connection_info.id, map)
        c.socket_obj = connection_info.socket_connection
        return c

    @classmethod
    def from_id(cls, id: int, map: Map) -> "Player":
        """
        Construct a person using id
        """
        c = cls(id, map)
        return c
