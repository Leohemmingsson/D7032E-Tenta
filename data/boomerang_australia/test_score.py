# std
from unittest.mock import patch

# own
from .score import count_throw_and_catch_score, collection_bonus, region_bonus, animal_bonus, site_bonus, activity_bonus
from .australia_card import AustraliaCard
from src.player_types import Bot, Player
from src.card import Deck, Card


def test_throw_and_catch_score_three_cards():
    player, all_cards = _get_player_and_deck()

    all_cards.add_card(Card(name="a", site="a", region="a", card_number=1))
    all_cards.add_card(Card(name="b", site="b", region="b", card_number=2))
    all_cards.add_card(Card(name="c", site="c", region="c", card_number=3))
    _add_deck_and_choose_cards(player, all_cards)

    assert count_throw_and_catch_score(player) == 2


def test_throw_and_catch_score_one_card():
    player, all_cards = _get_player_and_deck()

    all_cards.add_card(Card(name="a", site="a", region="a", card_number=1))
    _add_deck_and_choose_cards(player, all_cards)

    assert count_throw_and_catch_score(player) == 0


def test_throw_and_catch_score_wrong_order():
    player, all_cards = _get_player_and_deck()

    all_cards.add_card(Card(name="b", site="b", region="b", card_number=10))
    all_cards.add_card(Card(name="a", site="a", region="a", card_number=1))
    _add_deck_and_choose_cards(player, all_cards)

    assert count_throw_and_catch_score(player) == 9


def test_collection_bonus_under_seven():
    """ "
    1 + 1 + 1 = 3, 3 <= 7 => 3*2 = 6
    """
    player, all_cards = _get_player_and_deck()

    all_cards.add_card(
        AustraliaCard(name="a", site="a", region="a", card_number=1, collection="Leaves", animal="a", activity="a")
    )
    all_cards.add_card(
        AustraliaCard(name="b", site="b", region="b", card_number=2, collection="Leaves", animal="b", activity="b")
    )
    all_cards.add_card(
        AustraliaCard(name="c", site="c", region="c", card_number=3, collection="Leaves", animal="c", activity="c")
    )

    _add_deck_and_choose_cards(player, all_cards)

    assert collection_bonus(player) == 6


def test_collection_bonus_equals_seven():
    player, all_cards = _get_player_and_deck()

    all_cards.add_card(
        AustraliaCard(name="a", site="a", region="a", card_number=1, collection="Wildflowers", animal="a", activity="a")
    )
    all_cards.add_card(
        AustraliaCard(name="b", site="b", region="b", card_number=2, collection="Souvenirs", animal="b", activity="b")
    )

    _add_deck_and_choose_cards(player, all_cards)

    assert collection_bonus(player) == 14


def test_collection_bonus_over_seven():
    player, all_cards = _get_player_and_deck()

    all_cards.add_card(
        AustraliaCard(name="a", site="a", region="a", card_number=1, collection="Wildflowers", animal="a", activity="a")
    )
    all_cards.add_card(
        AustraliaCard(name="b", site="b", region="b", card_number=2, collection="Souvenirs", animal="b", activity="b")
    )
    all_cards.add_card(
        AustraliaCard(name="c", site="c", region="c", card_number=3, collection="Leaves", animal="c", activity="c")
    )

    _add_deck_and_choose_cards(player, all_cards)

    assert collection_bonus(player) == 8


def test_animal_bonus():
    player, all_cards = _get_player_and_deck()

    all_cards.add_card(
        AustraliaCard(name="a", site="a", region="a", card_number=1, collection="a", animal="Kangaroos", activity="a")
    )
    all_cards.add_card(
        AustraliaCard(name="b", site="b", region="b", card_number=2, collection="b", animal="Kangaroos", activity="b")
    )

    _add_deck_and_choose_cards(player, all_cards)

    assert animal_bonus(player) == 3


def test_animal_bonus_only_one_pair():
    player, all_cards = _get_player_and_deck()

    all_cards.add_card(
        AustraliaCard(name="a", site="a", region="a", card_number=1, collection="a", animal="Kangaroos", activity="a")
    )
    all_cards.add_card(
        AustraliaCard(name="b", site="b", region="b", card_number=2, collection="b", animal="Kangaroos", activity="b")
    )
    all_cards.add_card(
        AustraliaCard(name="c", site="c", region="c", card_number=3, collection="c", animal="Koalas", activity="c")
    )
    all_cards.add_card(
        AustraliaCard(name="d", site="d", region="d", card_number=4, collection="d", animal="Emus", activity="d")
    )

    _add_deck_and_choose_cards(player, all_cards)

    assert animal_bonus(player) == 3


def test_animal_bonus_multiple_pairs():
    player, all_cards = _get_player_and_deck()

    all_cards.add_card(
        AustraliaCard(name="a", site="a", region="a", card_number=1, collection="a", animal="Kangaroos", activity="a")
    )
    all_cards.add_card(
        AustraliaCard(name="b", site="b", region="b", card_number=2, collection="b", animal="Kangaroos", activity="b")
    )
    all_cards.add_card(
        AustraliaCard(name="c", site="c", region="c", card_number=3, collection="c", animal="Koalas", activity="c")
    )
    all_cards.add_card(
        AustraliaCard(name="d", site="d", region="d", card_number=4, collection="d", animal="Koalas", activity="d")
    )

    _add_deck_and_choose_cards(player, all_cards)

    assert animal_bonus(player) == 10


def test_animal_bonus_more_than_two_of_one():
    player, all_cards = _get_player_and_deck()

    all_cards.add_card(
        AustraliaCard(name="a", site="a", region="a", card_number=1, collection="a", animal="Kangaroos", activity="a")
    )
    all_cards.add_card(
        AustraliaCard(name="b", site="b", region="b", card_number=2, collection="b", animal="Kangaroos", activity="b")
    )
    all_cards.add_card(
        AustraliaCard(name="c", site="c", region="c", card_number=3, collection="c", animal="Kangaroos", activity="c")
    )
    all_cards.add_card(
        AustraliaCard(name="d", site="d", region="d", card_number=4, collection="d", animal="Kangaroos", activity="d")
    )

    _add_deck_and_choose_cards(player, all_cards)

    assert animal_bonus(player) == 3


@patch("builtins.input", side_effect=["Y"])
def test_activity_bonus(monkeypatch):
    player, all_cards = _get_player_and_deck()

    all_cards.add_card(
        AustraliaCard(
            name="a", site="a", region="a", card_number=1, collection="a", animal="a", activity="Indigenous Culture"
        )
    )
    all_cards.add_card(
        AustraliaCard(
            name="b", site="b", region="b", card_number=2, collection="b", animal="b", activity="Indigenous Culture"
        )
    )
    _add_deck_and_choose_cards(player, all_cards)

    assert activity_bonus(player) == 2


@patch("builtins.input", side_effect=["Y"])
def test_activity_bonus_not_same_acitvity(monkeypatch):
    player, all_cards = _get_player_and_deck()

    all_cards.add_card(
        AustraliaCard(
            name="a", site="a", region="a", card_number=1, collection="a", animal="a", activity="Indigenous Culture"
        )
    )
    all_cards.add_card(
        AustraliaCard(name="b", site="b", region="b", card_number=2, collection="b", animal="b", activity="Swimming")
    )
    _add_deck_and_choose_cards(player, all_cards)

    assert activity_bonus(player) == 0


@patch("builtins.input", side_effect=["Y"])
def test_activity_bonus_three_of_same(monkeypatch):
    player, all_cards = _get_player_and_deck()

    for _ in range(3):
        all_cards.add_card(
            AustraliaCard(
                name="a", site="a", region="a", card_number=1, collection="a", animal="a", activity="Indigenous Culture"
            )
        )

    _add_deck_and_choose_cards(player, all_cards)

    assert activity_bonus(player) == 4


@patch("builtins.input", side_effect=["Y"])
def test_activity_bonus_four_of_same(monkeypatch):
    player, all_cards = _get_player_and_deck()

    for _ in range(4):
        all_cards.add_card(
            AustraliaCard(
                name="a", site="a", region="a", card_number=1, collection="a", animal="a", activity="Indigenous Culture"
            )
        )

    _add_deck_and_choose_cards(player, all_cards)

    assert activity_bonus(player) == 7


@patch("builtins.input", side_effect=["Y"])
def test_activity_bonus_five_of_same(monkeypatch):
    player, all_cards = _get_player_and_deck()

    for _ in range(5):
        all_cards.add_card(
            AustraliaCard(
                name="a", site="a", region="a", card_number=1, collection="a", animal="a", activity="Indigenous Culture"
            )
        )
    _add_deck_and_choose_cards(player, all_cards)

    assert activity_bonus(player) == 10


@patch("builtins.input", side_effect=["Y"])
def test_activity_bonus_six_of_same(monkeypatch):
    player, all_cards = _get_player_and_deck()

    for _ in range(6):
        all_cards.add_card(
            AustraliaCard(
                name="a", site="a", region="a", card_number=1, collection="a", animal="a", activity="Indigenous Culture"
            )
        )
    _add_deck_and_choose_cards(player, all_cards)

    assert activity_bonus(player) == 15


# === helper functions === #
def _get_player_and_deck() -> tuple[Player, Deck]:
    player = Bot.from_id(1, None)
    return (player, Deck())


def _add_deck_and_choose_cards(player: Player, all_cards: Deck) -> None:
    player.add_deck_to_hand(all_cards)
    for _ in all_cards:
        player.choose_card()
