from ..player_types import Player


def send_dict_to_player(player: Player, data: dict) -> None:
    """
    Sends a dictionary to a player

    Args:
        player (Player): The player to send the data to
        data (dict): The data to send
    """
    send_value = ""
    for key, value in data.items():
        send_value += f"{key}:{value}, "

    player.send_message(send_value)
