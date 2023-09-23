# default
import os


def get_game_types() -> list:
    """
    This returns a list of the names of the folders in "data" folder.
    These are the game types one can play.
    """
    directories = []
    for _, dirs, _ in os.walk("./src/data"):
        directories = dirs
        break

    return directories
