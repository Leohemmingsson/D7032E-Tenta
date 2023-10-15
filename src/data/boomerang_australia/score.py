# std
from typing import Protocol

# pip
import yaml

# own
from player_types import Player


class MultiplePlayers(Protocol):
    """
    This is a alternetive to importing actual class to avoid circular imports.

    This is just mocking MultiplePlayers class to get better type hints.
    """

    def get_players_with_completed_region_bonus(self, taken: list[str]) -> list[Player]:
        ...


def count_throw_and_catch_score(one_player) -> int:
    """
    Takes one player and returns the throw and catch score
    """
    chosen_cards = one_player.all_chosen_cards
    diff_score = abs(chosen_cards[0].card_number - chosen_cards[-1].card_number)
    return diff_score


def region_bonus(players: MultiplePlayers, completed_regions: list, REGION_BONUS_SCORE: int) -> list:
    has_completed_regions = players.get_players_with_completed_region_bonus(completed_regions)
    for player in has_completed_regions:
        completed_regions = player.get_completed_regions_not_taken(completed_regions)
        for one_region in completed_regions:
            if one_region not in completed_regions:
                completed_regions.append(one_region)

            player.add_score(REGION_BONUS_SCORE, "Region bonus")

    return completed_regions


def collection_bonus(one_player: Player):
    bonuses = _get_collectives_bonus()
    all_cards = one_player.all_chosen_cards

    score = 0
    for one_card in all_cards:
        if one_card.collection is not None:
            collection_score = bonuses["collection"][one_card.collection]
            score += collection_score

    if score >= 7:
        return score
    return score * 2


def animal_bonus(one_player: Player):
    bonuses = _get_collectives_bonus()
    all_cards = one_player.all_chosen_cards

    previous_animals = set()
    pair_animals = set()
    for one_card in all_cards:
        if one_card.animal is None:
            continue
        if one_card.animal in previous_animals:
            pair_animals.add(one_card.animal)

        previous_animals.add(one_card.animal)

    score = 0
    for one_animal in pair_animals:
        score += bonuses["animal"][one_animal]

    return score


def _get_collectives_bonus() -> dict:
    path = "./src/data/boomerang_australia/collectives.yml"
    with open(path, "r") as file:
        values = yaml.safe_load(file)

    return values
