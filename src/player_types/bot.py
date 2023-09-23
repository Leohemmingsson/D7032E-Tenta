from data_structures import ClientConnectionInfo
from .player import Player


class Bot(Player):
    def __init__(self, connection_info: ClientConnectionInfo) -> None:
        super().__init__(connection_info)

    def send_message(self, message: str) -> None:
        pass
