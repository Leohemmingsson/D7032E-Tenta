from game import Boomerang


class BoomerangAustralia(Boomerang):
    def _set_constants(self) -> None:
        self._NR_OF_ROUNDS = 4
        self._CARDS_IN_HAND = 7
        self._REGION_BONUS_SCORE = 3
        self._taken_regions = []

    def _count_score_after_draft(self) -> None:
        has_completed_regions = self.players.get_players_with_completed_region_bonus(self._taken_regions)
        for player in has_completed_regions:
            completed_regions = player.get_completed_regions_not_taken(self._taken_regions)
            for one_region in completed_regions:
                if one_region not in self._taken_regions:
                    self._taken_regions.append(one_region)

                player.add_score(self._REGION_BONUS_SCORE)
                player.send_message("#####")
                player.send_message("# You got 3 points for completing a region.")
                player.send_message("")
        self._is_region_bonus_taken = True

    def _count_score_after_round(self) -> None:
        self.players.broadcast("#####")
        self.players.broadcast("# This rounds score:")
        self.players.count_and_divide_throw_and_catch_score()

        self.players.broadcast("")

    def _count_score_after_game(self) -> None:
        ...
