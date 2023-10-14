# import pytest


class TestRequirements:
    def test_player_count(self, monkeypatch):
        from ..initialize_game.user_selections import get_server_settings_from_user

        inputs = iter(["0", "1", "1"])

        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        result = get_server_settings_from_user
        assert result == "ok"

    def test_ass(self):
        assert 1 == 1
