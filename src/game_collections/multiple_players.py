import player_types
from .deck import Deck


class MultiplePlayers:
    """
    This will handle everything that every player should do at the same time.
    """

    def __init__(self, players: list[player_types.Player]) -> None:
        self.players = players

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

    def show_all_player_stats(self):
        for one_player in self.players:
            print(one_player.id)
            print(one_player.score)
            print("Cards in hand:")
            print(one_player.cards_in_hand)
            print("Cards chosen:")
            print(one_player.all_chosen_cards)
            print("------")
