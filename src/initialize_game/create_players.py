from player_types import Player, PersonPlayer, Bot
from data_structures import ClientConnectionInfo


def create_players(connection_info: list[ClientConnectionInfo] | None, bot_count: int) -> list[Player]:
    all_players = []
    counter = 0
    if connection_info is not None:
        for client_info in connection_info:
            all_players.append(PersonPlayer(client_info))
            counter += 1

    bots = _create_bots(bot_count, len(all_players))
    all_players.extend(bots)
    return all_players


def _create_bots(nr: int, id_from: int = 0) -> list[Player]:
    all_bots = []
    for i in range(nr):
        connection_info = ClientConnectionInfo(id_from + i, None, None)
        all_bots.append(Bot(connection_info))

    return all_bots
