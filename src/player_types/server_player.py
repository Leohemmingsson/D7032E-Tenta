from .player import Player


class ServerPlayer(Player):
    def send_message(self, message: str) -> None:
        print(message)
