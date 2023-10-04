# Pip package
import pandas as pd

from data_structures import Card
import random
from collections.abc import Iterator


class Deck:
    """
    A collection of cards.
    Can be initialized with a list of cards or a filename, only supports csv for now.
    """

    def __init__(self, cards: list[Card] | None = None, filename: str | None = None) -> None:
        self._validate_arguments(cards=cards, filename=filename)

        if cards is not None:
            self._cards = cards
        if filename is not None:
            self._cards = self._get_cards_from_csv(filename)
        if cards is None and filename is None:
            self._cards = []

    def __len__(self) -> int:
        return len(self._cards)

    def __repr__(self) -> str:
        col_len = 35
        col_len_after_field = 25
        repr_string = (
            f"{'Site [letter] (nr)':<{col_len_after_field}}"
            + "".join(
                [
                    f"{str(card.name) + ' [' + str(card.site) + ']' + ' (' + str(card.card_number) + ')':<{col_len}}"
                    for card in self._cards
                ]
            )
            + "\n"
        )

        for field in ["region", "collection", "animal", "activity"]:
            repr_string += (
                f"{field.capitalize():<{col_len_after_field}}"
                + "".join([f"{str(getattr(card, field)):<{col_len}}" for card in self._cards])
                + "\n"
            )
        return repr_string

    def __str__(self) -> str:
        return self.__repr__()

    def __iter__(self) -> Iterator[Card]:
        for card in self._cards:
            yield card

    def add_card(self, card: Card) -> None:
        """Add a card to the deck."""
        self._cards.append(card)

    def add_deck(self, deck: "Deck") -> None:
        """Add new deck in the back of the deck."""
        self._cards.extend(deck._cards)

    def shuffle(self) -> None:
        """Shuffle the deck."""
        random.shuffle(self._cards)

    def draw_first_card(self) -> Card:
        """Draw the first card from the deck. This means card will be removed from the deck."""
        if len(self._cards) == 0:
            raise ValueError("There are no cards in the deck.")
        return self._cards.pop(0)

    def pick_from_site(self, site: str | None = None) -> Card:
        """When choosing a card, the card will be removed from the deck."""

        if site is None:
            random_index = random.randint(0, len(self._cards) - 1)
            return self._cards.pop(random_index)
        else:
            index = self._get_index_of_site(site)
            return self._cards.pop(index)

    def _get_index_of_site(self, site: str) -> int:
        """Get the index of the site in the deck."""
        for i, e in enumerate(self._cards):
            if e.site == site:
                return i
        raise ValueError(f"Site {site} is not in the deck.")

    def _get_cards_from_csv(self, filename: str) -> list[Card]:
        created_cards = []

        df = pd.read_csv(filename)
        card_data: list[dict] = df.to_dict(orient="records")

        for element in card_data:
            card = Card(**element)
            created_cards.append(card)

        return created_cards

    def _validate_arguments(self, cards: list[Card] | None, filename: str | None) -> None:
        if cards is not None and filename is not None:
            raise ValueError("Either cards or filename must be specified, not both.")

        if type(cards) != list and cards is not None:
            raise TypeError(f"cards must be of [list | None] type, not {type(cards)}")

        if type(filename) != str and filename is not None:
            raise TypeError(f"filename must be of [str | None] type, not {type(filename)}")
