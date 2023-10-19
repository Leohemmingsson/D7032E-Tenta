import socket

from ..data_structures import ClientConnectionInfo, Map, Scoring
from ..card import Deck, Card


class Player:
    def __init__(self, id: int, map: Map) -> None:
        self._id = id
        self._map = map
        self._score = Scoring()
        self._hand = Deck()
        self._chosen_card = Deck()
        self._chosen_acitivity = []

    def send_message(self, message: str) -> None:
        """
        Sending a message to the player's terminal
        """
        raise NotImplementedError(f"Method not implemented for {type(self).__name__}")

    def show_cards_in_hand(self) -> None:
        """
        Showing the cards the player has in hand, this is like send_message but with the cards
        """
        raise NotImplementedError(f"Method not implemented for {type(self).__name__}")

    def choose_card(self) -> None:
        """
        Choosing a card from the hand and placing it in chosen cards
        """
        raise NotImplementedError(f"Method not implemented for {type(self).__name__}")

    def clear_screen(self) -> None:
        """
        This is to clear the screen of the player, nothing functional only makes it look better
        """
        raise NotImplementedError(f"Method not implemented for {type(self).__name__}")

    def ask(self, question: str) -> str:
        """
        This is a way to send custom questions to the player, and get a response
        """
        raise NotImplementedError(f"Method not implemented for {type(self).__name__}")

    @property
    def id(self) -> int:
        """
        Returns the id of the player
        """
        return self._id

    @property
    def socket_obj(self) -> socket.socket:
        """
        Socket connection used for communications to and from player,
        there is both a setter and getter
        """
        return self._socket

    @socket_obj.setter
    def socket_obj(self, value: socket.socket) -> None:
        self._socket = value

    @property
    def score(self) -> int:
        """
        Returns the score of the player
        """
        return int(self._score)

    @property
    def cards_in_hand(self) -> Deck:
        """
        Returns the cards in hand without side effects
        """
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

    @property
    def get_total_score_summary(self) -> dict:
        """
        Returns formatted string with score for each round divided into categories.
        """
        return self._score.summary

    @property
    def get_round_score_summary(self) -> str:
        """
        Returns formatted string with score of this round divided into categories.
        """
        return self._score.this_round_summary

    @property
    def get_round_score_summary_values(self) -> dict:
        return self._score.this_round_summary_values

    @property
    def visited_sites(self) -> list[str]:
        """
        Returns a list of all visited sites.
        """
        return self._map.get_all_visited_sites

    @property
    def nr_or_visited_sites(self) -> int:
        """
        Returns the total number of visited sites
        """
        return self._map.nr_of_visited_sites

    @property
    def get_chosen_activities(self) -> list[str]:
        """
        Returns a list of all chosen activities.
        """
        return self._chosen_acitivity

    def get_visited_sites_since_last_get(self) -> list[str]:
        """
        Resets the count for visited sites.
        """
        return self._map.get_visited_sites_since_last_get()

    def get_completed_regions_not_taken(self, taken: list[str]) -> list[str]:
        """
        This returns a list of all completed regions that are not taken.
        No side effects
        """
        return self._map.get_completed_regions_not_taken(taken)

    def add_score(self, value: int, reason: str) -> None:
        """
        This is a score ADDER, not setter
        """
        self._score.add_score(value, reason)

    def add_card_to_hand(self, card: Card) -> None:
        """
        Append a card to the hand (cards a player can choose)
        """
        self._hand.add_card(card)

    def add_deck_to_hand(self, deck: Deck) -> None:
        """
        Works as add card, but with a collection of cards (deck)
        """
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
        """
        Returns all cards that a player has in hand.
        The players hand will also be reset, so the hand is empty after this.
        """
        hand = self._hand
        self._hand = Deck()
        return hand

    def choose_activity(self, activity: str | None) -> None:
        self._chosen_acitivity.append(activity)

    def new_round(self):
        """
        This should be called when a new round starts.
        """
        self._score.new_round()

    def _choose_card_from_site(self, site: str) -> None:
        """
        Takes chosen card from hand and places in chosen cards.
        """
        card = self._hand.pick_from_site(site)
        self._add_card_to_chosen(card)

    def _choose_first_card(self) -> None:
        card = self._hand.draw_first_card()
        self._add_card_to_chosen(card)

    def _add_card_to_chosen(self, card: Card) -> None:
        self._map.visit_site(card.site)
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
