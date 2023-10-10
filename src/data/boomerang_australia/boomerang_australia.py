from game import Boomerang


class BoomerangAustralia(Boomerang):
    def _set_constants(self) -> None:
        self._NR_OF_ROUNDS = 4
        self._CARDS_IN_HAND = 7
        self._REGION_BONUS_SCORE = 3
        self._is_region_bonus_taken = False

    def _count_score_after_draft(self) -> None:
        if self._is_region_bonus_taken:
            return

        completed_region = self.players.get_players_with_completed_region_bonus
        if completed_region is not None:
            for player in completed_region:
                player.add_score(self._REGION_BONUS_SCORE)
            self.players.broadcast("Region bonus taken")
            self._is_region_bonus_taken = True

    def _count_score_after_round(self) -> None:
        self.players.broadcast("This rounds score:")
        self.players.count_and_divide_throw_and_catch_score()

    def _count_score_after_game(self) -> None:
        ...
