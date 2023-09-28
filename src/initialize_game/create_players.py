from player_types import Player, ServerPlayer, ClientPlayer, Bot
from data_structures import ClientConnectionInfo


def create_players(connection_info: list[ClientConnectionInfo] | None, bot_count: int) -> list[Player]:
    all_players = [ServerPlayer().from_id(0)]
    counter = 0
    if connection_info is not None:
        for client_info in connection_info:
            person = ClientPlayer.from_client_connection_info(client_info)
            all_players.append(person)
            counter += 1

    bots = _create_bots(bot_count, len(all_players))
    all_players.extend(bots)
    return all_players


def _create_bots(nr: int, id_from: int = 0) -> list[Player]:
    all_bots = []
    for i in range(nr):
        id = id_from + i
        new_bot = Bot().from_id(id)
        all_bots.append(new_bot)

    return all_bots
