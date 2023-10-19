# std
from typing import Protocol
from collections import defaultdict

# pip
import yaml

# own
from src.player_types import Player
from src.input_output import send_dict_to_player


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
    old_completed_regions = players.get_players_with_completed_region_bonus(completed_regions)
    for player in old_completed_regions:
        new_completed_regions = player.get_completed_regions_not_taken(completed_regions)
        for one_region in new_completed_regions:
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

    if score > 7:
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


def site_bonus(one_player: Player):
    score = len(one_player.get_visited_sites_since_last_get())
    return score


def activity_bonus(one_player: Player):
    bonuses = _get_collectives_bonus()
    chosen_activities = one_player.get_chosen_activities
    all_cards = one_player.all_chosen_cards
    activity_count = defaultdict(int)
    for one_card in all_cards:
        if one_card.activity is None:
            continue

        if one_card.activity not in chosen_activities:
            activity_count[one_card.activity] += 1

    one_player.send_message("Collected activities this round:")
    send_dict_to_player(one_player, activity_count)

    for one_activity in activity_count:
        count = activity_count[one_activity]
        score = bonuses["activity"][count]
        answer = one_player.ask(f"Want to keep {one_activity}({count}) [{score} points]? (Y/N)")
        one_player.send_message(f"Answer: {answer}")
        if answer == "Y" or answer == "y":
            one_player.choose_activity(one_activity)
            return score

    one_player.choose_activity(None)
    return 0


def _get_collectives_bonus() -> dict:
    path = "./data/boomerang_australia/collectives.yml"
    with open(path, "r") as file:
        values = yaml.safe_load(file)

    return values
