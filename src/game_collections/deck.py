# Pip package
import pandas as pd

from data_structures import Card
import random


class Deck:
    """
    A collection of cards.
    Can be initialized with a list of cards or a filename, only supports csv for now.
    """

    def __init__(self, cards: list[Card] | None = None, filename: str | None = None) -> None:
        self._validate_arguments(cards=cards, filename=filename)

        if cards is not None:
            self.cards = cards
        if filename is not None:
            self.cards = self._get_cards_from_csv(filename)

    def __len__(self) -> int:
        return len(self.cards)

    def add_card(self, card: Card) -> None:
        """Add a card to the deck."""
        self.cards.append(card)

    def shuffle(self) -> None:
        """Shuffle the deck."""
        random.shuffle(self.cards)

    def draw_first_card(self) -> Card:
        """Draw the first card from the deck. This means card will be removed from the deck."""
        if len(self.cards) == 0:
            raise ValueError("There are no cards in the deck.")
        return self.cards.pop(0)

    def pick_from_site(self, site: str | None = None) -> Card:
        """When choosing a card, the card will be removed from the deck."""

        if site is None:
            random_index = random.randint(0, len(self.cards) - 1)
            return self.cards.pop(random_index)
        else:
            index = self._get_index_of_site(site)
            return self.cards.pop(index)

    def _get_index_of_site(self, site: str) -> int:
        """Get the index of the site in the deck."""
        for i, e in enumerate(self.cards):
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
        if cards is None and filename is None:
            raise ValueError("Either cards or filename must be specified.")

        if cards is not None and filename is not None:
            raise ValueError("Either cards or filename must be specified, not both.")

        if type(cards) != list and cards is not None:
            raise TypeError(f"cards must be of [list | None] type, not {type(cards)}")

        if type(filename) != str and filename is not None:
            raise TypeError(f"filename must be of [str | None] type, not {type(filename)}")
