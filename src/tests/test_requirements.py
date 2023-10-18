# std
from unittest.mock import patch

# import pytest
from src.game import ContextLoader
from data.boomerang_australia import AustraliaCard


class TestRequirements:
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
        from src.game import create_game_from_context

        context = ContextLoader()
        game = create_game_from_context(context)
        assert game._CARDS_IN_HAND == 7

    @patch("builtins.input", side_effect=["0", "0", "1", "1"])
    def test_australia_rounds_settings(self, mock_input):
        from src.game import create_game_from_context

        context = ContextLoader()
        game = create_game_from_context(context)
        assert game._NR_OF_ROUNDS == 4
