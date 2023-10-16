# std
import os
from subprocess import call

# own
from .player import Player


class ServerPlayer(Player):
    def send_message(self, message: str) -> None:
        print(message)

    def show_cards_in_hand(self) -> None:
        print(self._hand)

    def choose_card(self) -> None:
        if len(self._hand) == 1:
            self._chosen_card.add_card(self._hand.draw_first_card())
        else:
            print("Choose card:")
            site = input()
            self._choose_card_from_site(site)

    def clear_screen(self) -> None:
        _ = call("clear" if os.name == "posix" else "cls")

    def ask(self, question: str) -> str:
        print(question)
        answer = input()
        return answer
