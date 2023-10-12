# std
from threading import Thread
from collections import deque

# own
import player_types
from .deck import Deck


class MultiplePlayers:
    """
    This will handle everything that every player should do at the same time.
    """

    def __init__(self, players: list[player_types.Player]) -> None:
        self.players = players

    def get_players_with_completed_region_bonus(self, taken: list[str]) -> list[player_types.Player]:
        players_with_completed_region_bonus = []
        for one_player in self.players:
            completed_regions = one_player.get_completed_regions_not_taken(taken)
            if len(completed_regions) > 0:
                players_with_completed_region_bonus.append(one_player)

        return players_with_completed_region_bonus

    def broadcast(self, message: str) -> None:
        """
        Sends the same message to all players.
        """
        for player in self.players:
            player.send_message(message)

    def deal_cards(self, deck: Deck, number_of_cards_each: int) -> None:
        """
        Deals one card for each player at a time, until everyone has the given amount of cards.
        """
        for _ in range(number_of_cards_each):
            for player in self.players:
                player.add_card_to_hand(deck.draw_first_card())

    def get_all_cards(self) -> Deck:
        """
        Returns all cards that all players have in their hands.
        Observer the cards are not shuffled.
        No player will have any cards left in their hand after this.
        """
        all_cards = Deck()
        for player in self.players:
            all_cards.add_deck(player.get_all_cards())
        return all_cards

    def show_each_player_their_cards(self) -> None:
        for player in self.players:
            player.show_cards_in_hand()

    def choose_cards(self) -> None:
        threads = []
        for player in self.players:
            one_thread = Thread(target=player.choose_card)
            one_thread.start()
            threads.append(one_thread)
        for one_thread in threads:
            one_thread.join()

    def rotate_cards_in_hand(self, reversed: bool = False) -> None:
        all_decks = []
        for player in self.players:
            all_decks.append(player.get_all_cards_in_hand())

        all_decks = deque(all_decks)
        rot = 1 if reversed else -1
        all_decks.rotate(rot)

        i = 0
        for player in self.players:
            player.add_deck_to_hand(all_decks[i])
            i += 1

    def clear_screen(self):
        for player in self.players:
            player.clear_screen()

    def show_all_players_draft(self):
        message = ""
        for player in self.players:
            if len(player.chosen_cards) == 0:
                continue
            message += f"Player {player.id}\n"
            message += str(player.chosen_cards)
            message += "------\n"

        self.broadcast(message)

    def count_and_divide_throw_and_catch_score(self):
        for one_player in self.players:
            chosen_cards = one_player.all_chosen_cards
            diff_score = abs(chosen_cards[0].card_number - chosen_cards[-1].card_number)
            one_player.add_score(diff_score, "Throw and catch")

    def new_round(self):
        for player in self.players:
            player.new_round()

    def show_results_and_winner(self):
        for player in self.players:
            score_summary = player.get_total_score_summary
            player.send_message(score_summary)

    def give_points(self, points: int, reason: str) -> None:
        for one_player in self.players:
            one_player.add_score(points, reason)

    def show_round_score_summary(self):
        for player in self.players:
            round_score_sumamry = player.get_round_score_summary
            player.send_message(round_score_sumamry)
