from .player import Player


class ServerPlayer(Player):
    def send_message(self, message: str) -> None:
        print(message)

    def show_cards_in_hand(self) -> None:
        print(self.hand)

    def choose_card(self) -> None:
        print("Choose card:")
        site = input()
        self._choose_card_from_site(site)
