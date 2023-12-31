from src.game import Boomerang
from .score import count_throw_and_catch_score, collection_bonus, region_bonus, animal_bonus, site_bonus, activity_bonus


class BoomerangAustralia(Boomerang):
    def _set_constants(self) -> None:
        self._NR_OF_ROUNDS = 4
        self._CARDS_IN_HAND = 7
        self._REGION_BONUS_SCORE = 3
        self._completed_regions = []

    def _count_score_after_draft(self) -> None:
        self._completed_regions = region_bonus(self.players, self._completed_regions, self._REGION_BONUS_SCORE)

    def _count_score_after_round(self) -> None:
        self.players.count_and_divide_score_with_func("Throw and catch", count_throw_and_catch_score)
        self.players.count_and_divide_score_with_func("Collection bonus", collection_bonus)
        self.players.count_and_divide_score_with_func("Animal bonus", animal_bonus)
        self.players.count_and_divide_score_with_func("Activity bonus", activity_bonus)
        self.players.count_and_divide_score_with_func("New site visited", site_bonus)

        self.players.broadcast("")

    # def _count_score_after_game(self) -> None:
    # self.players.count_and_divide_score_with_func("New site visited", site_bonus)
