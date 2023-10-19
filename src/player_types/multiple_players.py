# std
from threading import Thread
from typing import Callable

# own
from .player import Player
from ..card import Deck
from ..utils import rotate_list


class MultiplePlayers:
    """
    This is a wrapper class for a list of players, to make it seemless to work with multiple players.
    """

    def __init__(self, players: list[Player]) -> None:
        self._players = players

    @property
    def players(self) -> list[Player]:
        """
        Getter for players, this is only used for testing
        """
        return self._players

    def get_players_with_completed_region_bonus(self, taken: list[str]) -> list[Player]:
        """
        Returns a list of players that have completed regions that are not taken.
        No side effects.
        """
        players_with_completed_region_bonus = []
        for one_player in self._players:
            completed_regions = one_player.get_completed_regions_not_taken(taken)
            if len(completed_regions) > 0:
                players_with_completed_region_bonus.append(one_player)

        return players_with_completed_region_bonus

    def broadcast(self, message: str) -> None:
        """
        Sends the same message to all players.
        """
        for player in self._players:
            player.send_message(message)

    def deal_cards(self, deck: Deck, number_of_cards_each: int) -> None:
        """
        Deals one card for each player at a time, until everyone has the given amount of cards.
        """
        for _ in range(number_of_cards_each):
            for player in self._players:
                player.add_card_to_hand(deck.draw_first_card())

    def get_all_cards(self) -> Deck:
        """
        Returns all cards that all players have in their hands.
        Observer the cards are not shuffled.
        No player will have any cards left in their hand after this.
        """
        all_cards = Deck()
        for player in self._players:
            all_cards.add_deck(player.get_all_cards())
        return all_cards

    def show_each_player_their_cards(self) -> None:
        for player in self._players:
            player.show_cards_in_hand()

    def choose_cards(self) -> None:
        """
        Creates one thread per player so each player can choose a card.
        When everyone has chosen a card (simultaneously), the function is done
        """
        threads = []
        for player in self._players:
            one_thread = Thread(target=player.choose_card)
            one_thread.start()
            threads.append(one_thread)
        for one_thread in threads:
            one_thread.join()

    def rotate_cards_in_hand(self, reversed: bool = False) -> None:
        """
        This rotates the cards between the players.
        So one player get another players cards, and so on.
        """
        all_decks = []
        for player in self._players:
            all_decks.append(player.get_all_cards_in_hand())

        all_decks = rotate_list(all_decks, reversed)

        i = 0
        for player in self._players:
            player.add_deck_to_hand(all_decks[i])
            i += 1

    def clear_screen(self):
        """
        Cosmetic feature to clean screen.
        """
        for player in self._players:
            player.clear_screen()

    def show_all_players_draft(self):
        """
        Show all players draft to all players.
        (Every player sees the same thing)
        """
        message = ""
        for player in self._players:
            if len(player.chosen_cards) == 0:
                continue
            message += f"Player {player.id}\n"
            message += str(player.chosen_cards)
            message += "------\n"

        self.broadcast(message)

    def show_visited_sites(self):
        """
        Inidividually show players their visited sites.
        """
        for one_player in self._players:
            visited_sites = one_player.visited_sites
            one_player.send_message(f"visited_sites: \n{visited_sites}")

    def count_and_divide_score_with_func(self, score_name: str, func: Callable) -> None:
        """
        This is a wrapper function to count and divide score for each player.
        So when giving a scoring function, this will be done for each player.
        """
        threads = []
        for one_player in self._players:
            one_thread = Thread(target=self._count_and_div_score_one_player, args=(one_player, score_name, func))
            one_thread.start()
            threads.append(one_thread)
        for one_thread in threads:
            one_thread.join()

    def _count_and_div_score_one_player(self, one_player: Player, score_name: str, func: Callable) -> None:
        diff_score = func(one_player)
        one_player.add_score(diff_score, score_name)

    def new_round(self):
        for player in self._players:
            player.new_round()

    def show_results_and_winner(self):
        """
        Displays first each of the players personal score summary.
        Then displays the winner.
        """
        winner = {}
        for player in self._players:
            score_summary = player.get_total_score_summary
            last_round_score = player.get_round_score_summary_values
            if "score" not in winner or score_summary["score"] > winner["score"]:
                winner = {
                    "id": player.id,
                    "score": score_summary["score"],
                    "throw_and_catch_score": last_round_score["Throw and catch"],
                }
            if score_summary["score"] == winner["score"]:
                if last_round_score["Throw and catch"] > winner["throw_and_catch_score"]:
                    winner = {
                        "id": player.id,
                        "score": score_summary["score"],
                        "throw_and_catch_score": last_round_score["Throw and catch"],
                    }
            player.send_message(score_summary["repr"])

        self.broadcast(f"Winner is player {winner['id']} with {winner['score']} points!")

    def give_points(self, points: int, reason: str) -> None:
        for one_player in self._players:
            one_player.add_score(points, reason)

    def show_round_score_summary(self):
        for player in self._players:
            round_score_sumamry = player.get_round_score_summary
            player.send_message(round_score_sumamry)
