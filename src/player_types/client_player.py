from .player import Player
from ..connection import send_message_to, get_full_message


class ClientPlayer(Player):
    def send_message(self, message: str) -> None:
        send_message_to(self.socket_obj, message)

    def show_cards_in_hand(self) -> None:
        send_message_to(self.socket_obj, "Cards in hand:")
        send_message_to(self.socket_obj, str(self._hand))

    def choose_card(self) -> None:
        if len(self._hand) == 1:
            self._choose_first_card()
        else:
            send_message_to(self.socket_obj, "Choose card:", is_question=True)
            site = get_full_message(self.socket_obj)
            self._choose_card_from_site(site["message"])

    def clear_screen(self) -> None:
        send_message_to(self.socket_obj, "clear", special=True)

    def ask(self, question: str) -> str:
        send_message_to(self.socket_obj, question, is_question=True)
        answer = get_full_message(self.socket_obj)
        return answer["message"]
