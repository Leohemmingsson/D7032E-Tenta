from boomerang import Boomerang
from player_types.Player import Player


class BoomerangAustralia(Boomerang):
    def __init__(self, players: list[Player]):
        self.cards_file = "src/cards/boomerang_australia.csv"
        super().__init__(players)

    def _get_initialized_deck(self):
        pass
