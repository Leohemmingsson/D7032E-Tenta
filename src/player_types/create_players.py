from .player import Player
from .server_player import ServerPlayer
from .client_player import ClientPlayer
from .bot import Bot
from ..data_structures import ClientConnectionInfo, Map


def create_players(connection_info: list[ClientConnectionInfo] | None, bot_count: int, deck_path: str) -> list[Player]:
    """
    Depending on the connection_info, and bot_count this will create a list of players of different types.
    """
    all_players = [ServerPlayer.from_id(0, Map(deck_path))]
    if connection_info is not None:
        for client_info in connection_info:
            person = ClientPlayer.from_client_connection_info(client_info, Map(deck_path))
            all_players.append(person)

    bots = _create_bots(bot_count, len(all_players), deck_path=deck_path)
    all_players.extend(bots)
    return all_players


def _create_bots(nr: int, id_from: int = 0, deck_path: str = "") -> list[Player]:
    all_bots = []
    for i in range(nr):
        id = id_from + i
        new_bot = Bot.from_id(id, Map(deck_path))
        all_bots.append(new_bot)

    return all_bots
