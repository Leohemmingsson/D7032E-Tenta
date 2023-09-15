from dataclasses import dataclass


@dataclass
class Card:
    """
    This is just playing cards which contains different values etc.
    """

    name: str
    site: str
    region: str
    card_number: int
    collection: str
    animal: str
    activity: str
