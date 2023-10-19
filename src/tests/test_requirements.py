# std
from unittest.mock import patch

# import pytest
from src.game import ContextLoader, create_game_from_context
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
