from connection import run_client


def main():
    print("[0] Create a new game\n[1] Join an existing game")
    choice = ""
    while choice != "0" and choice != "1":
        choice = input("Enter your choice: ")
        match choice:
            case "0":
                print("Creating a new game...")
                _initialize_server()
            case "1":
                while True:
                    port = input("Enter the port number (Empty for default): ")
                    if port == "":
                        port = None
                    _join_game(port)


def _initialize_server():
    ...


def _join_game(port: str | None):
    try:
        run_client(port)
    except ConnectionRefusedError:
        print(f"Connection refused. Make sure the server is running on port {port}")


if __name__ == "__main__":
    main()
