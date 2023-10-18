# own imports
from ..card import Deck
from ..connection import Server
from ..input_output import get_server_settings_from_user, get_package_from_user
from ..utils import get_dir_in_path
from ..data_structures import PackageData
from ..player_types import MultiplePlayers, create_players


class ContextLoader:
    """
    Getting values from user and loads relevant data, including creating the server.
    This is the "connection" between different parts of the program, where everything is initialized.
    """

    def __init__(self):
        self._data_folder_name = "./data/"
        self._server_settings = get_server_settings_from_user()
        all_package_paths = get_dir_in_path(self._data_folder_name)
        all_package_types = [PackageData(self._data_folder_name + path) for path in all_package_paths]
        self._package = get_package_from_user(all_package_types)
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
    def class_name(self) -> str:
        return self._package.class_name

    @property
    def card_class_name(self) -> str:
        return self._package.card_class_name

    @property
    def packet_path(self) -> str:
        return self._package.path

    @property
    def _deck_path(self) -> str:
        return self._package.deck_path

    @property
    def all_players(self) -> MultiplePlayers:
        """
        Starts the server listens for clients and creates players.
        """
        clients_connection_info = self._server.start_server(self.client_count)
        list_of_players = create_players(clients_connection_info, self.bot_count, self._deck_path)
        all_players = MultiplePlayers(list_of_players)

        return all_players

    def deck(self, CardClass) -> Deck:
        deck = Deck(filename=self._deck_path, CardClass=CardClass)
        deck.shuffle()
        return deck
