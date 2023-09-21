from connection import Client, Server, broadcast_message_to


def main():
    print("[0] Create a new game\n[1] Join an existing game")
    choice = ""
    while choice != "0" and choice != "1":
        choice = input("Enter your choice: ")
        match choice:
            case "0":
                port = _get_game_port_number_from_user()
                print("Creating a new game on port {port}...")
                _initialize_server(port)
            case "1":
                port = _get_game_port_number_from_user()
                _join_game(port)


def _initialize_server(port: int | None) -> None:
    server = Server(port)
    try:
        all_clients = server.start_server(2)
    except OSError:
        print("Port already in use. Try again.")
        return

    while True:
        user_message = input()
        if "exit" in user_message:
            server.close_server()
            exit()
        broadcast_message_to(all_clients, user_message)
        if "reply" in user_message:
            x = server.get_answers_from_clients(all_clients)
            print(f"{x}")


def _join_game(port: int | None):
    client = Client(port)
    try:
        client.run_client()
    except ConnectionRefusedError:
        print(f"Connection refused. Make sure the server is running on port {port}")


def _get_game_port_number_from_user() -> int | None:
    port: int = 0
    while port == 0:
        user_input = input("Enter the port number (Empty for default): ")
        try:
            port = int(user_input)
        except ValueError:
            if user_input == "":
                return None
    return port


if __name__ == "__main__":
    main()
