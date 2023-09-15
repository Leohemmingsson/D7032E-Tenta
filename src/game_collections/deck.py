# Pip package
import pandas as pd

from datatypes import Card
from random import randint


class Deck:
    """
    A collection of cards.
    Can be initialized with a list of cards or a filename, only supports csv for now.
    """

    def __init__(
        self, cards: list[Card] | None = None, filename: str | None = None
    ) -> None:
        self._validate_arguments(cards, filename)

        if cards is not None:
            self.cards = cards
        if filename is not None:
            self.cards = self._get_cards_from_csv(filename)

    def add_card(self, card: Card) -> None:
        """Add a card to the deck."""
        self.cards.append(card)

    def shuffle(self) -> None:
        """Shuffle the deck."""
        pass

    def draw(self, site: str | None = None) -> Card:
        """
        Args:
            site (str): The site to draw from. If None, draw random card.

        Returns:
            Card: The card drawn. This means that the card will be remoed from the deck.
        """

        if site is None:
            random_index = randint(0, len(self.cards) - 1)
            return self.cards.pop(random_index)
        else:
            index = self._get_index_of_site(site)
            if index is None:
                raise ValueError(f"Site {site} is not in the deck.")
            return self.cards.pop(index)

    def _get_index_of_site(self, site: str) -> int | None:
        """Get the index of the site in the deck."""
        for i, e in enumerate(self.cards):
            if e.site == site:
                return i
        return None

    def _get_cards_from_csv(self, filename: str) -> list[Card]:
        # df = pd.read_csv(filename)
        # card_data = df.to_dict(orient="records")

        return cards

    def _validate_arguments(
        self, cards: list[Card] | None, filename: str | None
    ) -> None:
        if cards is None and filename is None:
            raise ValueError("Either cards or filename must be specified.")

        if cards is not None and filename is not None:
            raise ValueError("Either cards or filename must be specified, not both.")

        if type(cards) != list or cards is not None:
            raise TypeError(f"cards must be of list | None type, not {type(cards)}")

        if type(filename) != str or filename is not None:
            raise TypeError(
                f"filename must be of str | None type, not {type(filename)}"
            )
