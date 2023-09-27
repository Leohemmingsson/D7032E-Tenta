"""
All initial user selections are handled here.
"""


def is_server() -> bool:
    """
    Starting menu for game, through termnial input.
    """
    print("[0] Create a new game\n[1] Join an existing game")

    choice = ""
    while choice != "0" and choice != "1":
        choice = input("Enter your choice: ")
        match choice:
            case "0":
                return True

            case "1":
                return False
    raise ValueError("Invalid choice")


def get_server_settings_from_user() -> dict:
    """
    This should be all settings in order to create a server.

    Returns:
        dict:
            port: int | None
            client_count: int
            bot_count: int
    """
    port = _get_game_port_number_from_user()
    client_count, bot_count = _get_player_count_from_user()

    return {"port": port, "client_count": client_count, "bot_count": bot_count}


def get_client_port_from_user() -> int | None:
    """
    Asks the user for the port number of the game they want to join.

    Returns:
        port: int | None
    """
    return _get_game_port_number_from_user()


def get_game_folder_name_from_user(alternatives: list) -> str:
    """
    Asks the user what game to launch. Ex boomerang australia or boomerang america

    Returns:
        path: str
    """
    print("Choose one of the following:")
    for index, alternative in enumerate(alternatives):
        print(f"[{index}] {alternative}")

    index = -1
    while index not in range(len(alternatives)):
        index = _get_int_error_handled("Enter your choice: ")

    return alternatives[index]


def _get_game_port_number_from_user() -> int | None:
    question = "Enter the port number (Empty or 0 is default): "
    port = _get_int_error_handled(question)
    if port == 0:
        port = None
    return port


def _get_player_count_from_user() -> tuple[int, int]:
    while True:
        question = "Enter the number of other players (clients): "
        players = _get_int_error_handled(question)

        question = "Enter the number of bots: "
        bots = _get_int_error_handled(question)

        if _is_valid_player_count(players, bots):
            return players, bots
        else:
            print("Invalid player count. Total player count must be between 2 and 4")


def _is_valid_player_count(players: int, bots: int) -> bool:
    """
    Making sure player count is between 2 and 4, including the one who created the game.
    So actual limits are between 1 and 3
    """
    if players + bots < 1 or players + bots > 3:
        return False
    return True


def _get_int_error_handled(question: str) -> int:
    value: int = 0
    while True:
        user_input = input(question)
        try:
            value = int(user_input)
            return value
        except ValueError:
            if user_input == "":
                return 0
