import game_collections
from connection import Server
from .create_players import create_players
from .user_selections import get_server_settings_from_user, get_packet_from_user
from .read_file_structure import get_dir_in_path
from data_structures import PacketData


class ContextLoader:
    """
    Getting values from user and loads relevant data, including creating the server.
    This is the "connection" between different parts of the program, where everything is initialized.
    """

    def __init__(self):
        self._data_folder_name = "./src/data/"
        self._server_settings = get_server_settings_from_user()
        all_packet_paths = get_dir_in_path(self._data_folder_name)
        all_packet_types = [PacketData(self._data_folder_name + path) for path in all_packet_paths]
        self.packet = get_packet_from_user(all_packet_types)
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
        return self.packet.class_name

    @property
    def packet_path(self) -> str:
        return self.packet.path

    @property
    def all_players(self) -> game_collections.MultiplePlayers:
        """
        Starts the server listens for clients and creates players.
        """
        clients_connection_info = self._server.start_server(self.client_count)
        list_of_players = create_players(clients_connection_info, self.bot_count)
        all_players = game_collections.MultiplePlayers(list_of_players)

        return all_players

    @property
    def deck(self) -> game_collections.Deck:
        deck = game_collections.Deck(filename=self.packet.deck_path)
        deck.shuffle()
        return deck
