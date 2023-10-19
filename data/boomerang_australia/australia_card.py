# std
from dataclasses import dataclass

# own
from src.card import Card as BaseCard


@dataclass(kw_only=True)
class AustraliaCard(BaseCard):
    region: str
    collection: str
    animal: str
    activity: str
