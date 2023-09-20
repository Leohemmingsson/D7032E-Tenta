from boomerang import Boomerang
from player_types.player import Player


class BoomerangAustralia(Boomerang):
    def server_run(self, players: list[Player]):
        super().init_server(players)

    def _get_initialized_deck(self):
        pass

    @property
    def _cards_file(self):
        return "src/cards/boomerang_australia.csv"
