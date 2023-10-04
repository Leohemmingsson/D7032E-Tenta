from .player import Player
from connection import send_message_to, get_full_message


class ClientPlayer(Player):
    def send_message(self, message: str) -> None:
        send_message_to(self.socket_obj, message)

    def show_cards_in_hand(self) -> None:
        send_message_to(self.socket_obj, "Cards in hand:")
        send_message_to(self.socket_obj, str(self.hand))

    def choose_card(self) -> None:
        send_message_to(self.socket_obj, "Choose card:")
        site = get_full_message(self.socket_obj)
        self._choose_card_from_site(site)
