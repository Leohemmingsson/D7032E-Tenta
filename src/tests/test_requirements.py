# std
from unittest.mock import patch

# import pytest
from src.game import ContextLoader, create_game_from_context
from src.data_structures import Scoring
from data.boomerang_australia import AustraliaCard


class TestRequirements:
    """
    Testing the requirements for the game.
    When using side_effect in patch, the values can be considered as user input.
    The combination of 0, 0, 1, 1 is used to create a boomerang_australia game (given settings rigth now),
    with one bot and the server player
    """

    @patch("builtins.input", side_effect=["0", "0", "0"])
    def test_start_game_zero_players(self, mock_input, capfd):
        from src.input_output import is_valid_player_count

        values = [(0, 0), (2, 2), (3, 1), (1, 3), (4, 0), (0, 4)]
        for player, bot in values:
            assert not is_valid_player_count(player, bot)

    def test_valid_player_count(self):
        from src.input_output import is_valid_player_count

        values = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2), (3, 0), (0, 3)]
        for player, bot in values:
            assert is_valid_player_count(player, bot)

    @patch("builtins.input", side_effect=["0", "0", "1", "1"])
    def test_count_cards_in_australia(self, mock_input):
        context = ContextLoader()
        deck = context.deck(AustraliaCard)
        assert len(deck) == 28

    @patch("builtins.input", side_effect=["0", "0", "1", "1"])
    def test_shuffle_deck(self, mock_input):
        """
        Observe that this test can fail, but it is very unlikely.
        Reason being that there is a rist that the deck is shuffled back to the same order.
        If this were to happnen, buy a triss ;)
        """
        context = ContextLoader()
        assert context.deck(AustraliaCard).__repr__() != context.deck(AustraliaCard).__repr__()

    @patch("builtins.input", side_effect=["0", "0", "1", "1"])
    def test_dealing_cards_work(self, mock_input):
        context = ContextLoader()
        players = context.all_players

        players.deal_cards(context.deck(AustraliaCard), 7)

        for player in players.players:
            assert len(player.cards_in_hand) == 7

    @patch("builtins.input", side_effect=["0", "0", "1", "1"])
    def test_australia_dealing_settings(self, mock_input):
        """
        This makes sure that the variables are correct.
        """
        context = ContextLoader()
        game = create_game_from_context(context)
        assert game._CARDS_IN_HAND == 7

    @patch("builtins.input", side_effect=["0", "0", "1", "1"])
    def test_dealing_cards(self, mock_input):
        context = ContextLoader()
        players = context.all_players

        players.deal_cards(context.deck(AustraliaCard), 7)

        for player in players.players:
            assert len(player.cards_in_hand) == 7

    @patch("builtins.input", side_effect=["0", "0", "1", "1"])
    def test_australia_rounds_settings(self, mock_input):
        """
        This makes sure that the variables are correct.
        """
        context = ContextLoader()
        game = create_game_from_context(context)
        assert game._NR_OF_ROUNDS == 4

    def test_scoring_system(self):
        x = Scoring()
        x.new_round()
        for _ in range(4):
            x.add_score(1, "New site")
        x.new_round()
        for _ in range(4):
            x.add_score(1, "New site")

        assert x.score == 8

    def test_scoring_mulitple_types(self):
        x = Scoring()
        x.new_round()
        for _ in range(4):
            x.add_score(1, "New site")
        x.new_round()
        for _ in range(4):
            x.add_score(3, "Region bonus")

        assert x.score == 16

    def test_scoring_one_time_multiple_rounds(self):
        x = Scoring()
        for _ in range(4):
            x.new_round()
        x.add_score(1, "New site")

        assert x.score == 1

    def test_winner_highest_score(self):
        from src.player_types import Bot, MultiplePlayers

        player = Bot.from_id(1, None)
        player.new_round()
        player.add_score(1, "Throw and catch")
        player.add_score(6, "Region bonus")
        player.add_score(3, "Region bonus")
        player2 = Bot.from_id(2, None)
        player2.new_round()
        player2.add_score(7, "Throw and catch")
        player2.add_score(1, "New site")
        all_players = MultiplePlayers([player, player2])
        winner_id = all_players.show_results_and_winner()
        assert winner_id == player.id

    def test_winner_highest_score2(self):
        from src.player_types import Bot, MultiplePlayers

        player = Bot.from_id(1, None)
        player.new_round()
        player.add_score(7, "Throw and catch")
        player.add_score(3, "Region bonus")
        player.add_score(3, "Region bonus")
        player2 = Bot.from_id(2, None)
        player2.new_round()
        player2.add_score(1, "Throw and catch")
        player2.add_score(1, "New site")
        player2.add_score(15, "Animal bonus")
        all_players = MultiplePlayers([player, player2])
        winner_id = all_players.show_results_and_winner()
        assert winner_id == player2.id

    def test_tie(self):
        from src.player_types import Bot, MultiplePlayers

        player = Bot.from_id(1, None)
        player.new_round()
        player.add_score(1, "Throw and catch")
        player.add_score(1, "New site")
        player.add_score(1, "New site")
        player.add_score(1, "New site")
        player.add_score(1, "New site")
        player2 = Bot.from_id(2, None)
        player2.new_round()
        player2.add_score(4, "Throw and catch")
        player2.add_score(1, "New site")
        all_players = MultiplePlayers([player, player2])
        winner_id = all_players.show_results_and_winner()
        assert winner_id == player2.id

    def test_tie_other_order(self):
        from src.player_types import Bot, MultiplePlayers

        player = Bot.from_id(1, None)
        player.new_round()
        player.add_score(3, "Throw and catch")
        player.add_score(1, "New site")
        player2 = Bot.from_id(2, None)
        player2.new_round()
        player2.add_score(2, "Throw and catch")
        player.add_score(1, "New site")
        player2.add_score(1, "New site")
        all_players = MultiplePlayers([player, player2])
        winner_id = all_players.show_results_and_winner()
        assert winner_id == player.id
