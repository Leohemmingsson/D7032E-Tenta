# import pytest

from unittest.mock import patch


class TestRequirements:
    def test_non_valid_player_count(self):
        from src.input_output import is_valid_player_count

        values = [(0, 0), (2, 2), (3, 1), (1, 3), (4, 0), (0, 4)]
        for player, bot in values:
            assert not is_valid_player_count(player, bot)

    def test_valid_player_count(self):
        from src.input_output import is_valid_player_count

        values = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2), (3, 0), (0, 3)]
        for player, bot in values:
            assert is_valid_player_count(player, bot)

    @patch("builtins.input", side_effect=["0", "0", "0", "1"])
    def test_count_cards_in_australia(self, mock_input):
        from src.initialize_game import ContextLoader

        context = ContextLoader()
        print(context.deck)
