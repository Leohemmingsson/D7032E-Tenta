from game import Boomerang
from connection import Client
from initialize_game import (
    ContextLoader,
    is_server,
    get_client_port_from_user,
)


def main() -> None:
    if is_server():
        context = ContextLoader()

        game = Boomerang(context.all_players, context.deck)

        game.start_game()

    else:
        port = get_client_port_from_user()
        client = Client(port)
        client.run_client()


if __name__ == "__main__":
    main()
