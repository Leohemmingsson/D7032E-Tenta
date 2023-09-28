from .player import Player
from connection import send_message_to


class ClientPlayer(Player):
    def send_message(self, message: str) -> None:
        send_message_to(self.socket_obj, message)
