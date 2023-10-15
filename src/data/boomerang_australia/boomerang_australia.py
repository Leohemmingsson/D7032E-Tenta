from game import Boomerang
from .score import count_throw_and_catch_score, collection_bonus, region_bonus, animal_bonus


class BoomerangAustralia(Boomerang):
    def _set_constants(self) -> None:
        self._NR_OF_ROUNDS = 4
        self._CARDS_IN_HAND = 7
        self._REGION_BONUS_SCORE = 3
        self._completed_regions = []

    def _count_score_after_draft(self) -> None:
        self._completed_regions = region_bonus(self.players, self._completed_regions, self._REGION_BONUS_SCORE)
        # visited sites

    def _count_score_after_round(self) -> None:
        self.players.count_and_divide_score_with_func("Throw and catch", count_throw_and_catch_score)
        self.players.count_and_divide_score_with_func("Collection bonus", collection_bonus)
        self.players.count_and_divide_score_with_func("Animal bonus", animal_bonus)

        self.players.broadcast("")
