from src.connection import Client
from src.game import create_game_from_context
from src.initialize_game import ContextLoader
from src.input_output import is_server, get_client_port_from_user


def main() -> None:
    if is_server():
        context = ContextLoader()

        game = create_game_from_context(context)

        game.start_game()

    else:
        port = get_client_port_from_user()
        client = Client(port)
        client.run_client()


if __name__ == "__main__":
    main()