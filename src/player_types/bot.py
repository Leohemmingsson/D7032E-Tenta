from .player import Player


class Bot(Player):
    def send_message(self, message: str) -> None:
        pass

    def show_cards_in_hand(self) -> None:
        pass

    def choose_card(self) -> None:
        self._choose_first_card()
