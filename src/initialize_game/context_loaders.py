from game_collections import Deck, MultiplePlayers
from connection import Server
from .create_players import create_players
from .user_selections import get_server_settings_from_user, get_game_folder_name_from_user
from .read_file_structure import get_dir_in_path


class ContextLoader:
    """
    Getting values from user and loads relevant data, including creating the server.
    This is the "connection" between different parts of the program, where everything is initialized.
    """

    def __init__(self):
        self._server_settings = get_server_settings_from_user()
        all_game_types = get_dir_in_path("./data")
        self._game_folder_name = "./data/" + get_game_folder_name_from_user(all_game_types)
        self._deck_filename = self._game_folder_name + "/cards.csv"
        self._server = Server(self.port)

    @property
    def port(self) -> int | None:
        return self._server_settings["port"]

    @property
    def client_count(self) -> int:
        return self._server_settings["client_count"]

    @property
    def bot_count(self) -> int:
        return self._server_settings["bot_count"]

    @property
    def all_players(self) -> MultiplePlayers:
        """
        Starts the server listens for clients and creates players.
        """
        clients_connection_info = self._server.start_server(self.client_count)
        list_of_players = create_players(clients_connection_info, self.bot_count)
        all_players = MultiplePlayers(list_of_players)

        return all_players

    @property
    def deck(self) -> Deck:
        deck = Deck(filename=self._deck_filename)
        deck.shuffle()
        return deck
