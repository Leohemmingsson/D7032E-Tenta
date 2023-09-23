from game import Boomerang
from connection import Client, Server
from game_collections import Deck
from initialize_game import (
    get_server_settings_from_user,
    is_server_from_user,
    get_client_port_from_user,
    get_game_folder_name_from_user,
    create_players,
    get_game_types,
)


def main() -> None:
    """
    Setups the game, starting gameloop and connecting all players
    """

    if is_server_from_user():
        # Get all user input
        server_settings = get_server_settings_from_user()
        all_game_types = get_game_types()
        game_folder_name = "./src/data/" + get_game_folder_name_from_user(all_game_types)

        # Start server
        server = Server(server_settings["port"])
        clients_connection_info = server.start_server(server_settings["client_count"])

        # create objects
        all_players = create_players(clients_connection_info, server_settings["bot_count"])
        deck_filename = game_folder_name + "/cards.csv"
        deck = Deck(filename=deck_filename)
        game = Boomerang(all_players, deck)

        game.start_game()

    else:
        port = get_client_port_from_user()
        client = Client(port)
        client.run_client()


if __name__ == "__main__":
    main()
