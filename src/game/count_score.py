from game_collections import MultiplePlayers


def region_bonus(players: MultiplePlayers, completed_regions: list, REGION_BONUS_SCORE: int) -> list:
    has_completed_regions = players.get_players_with_completed_region_bonus(completed_regions)
    for player in has_completed_regions:
        completed_regions = player.get_completed_regions_not_taken(completed_regions)
        for one_region in completed_regions:
            if one_region not in completed_regions:
                completed_regions.append(one_region)

            player.add_score(REGION_BONUS_SCORE, "Region bonus")

    return completed_regions


# This will become a issue, with circular imports when using MultiplePlayers
# and this function doing the logic for MultiplePlayers....
#
#
def count_and_divide_throw_and_catch_score(self) -> None:
    for player in self:
        player.count_and_divide_throw_and_catch_score()
