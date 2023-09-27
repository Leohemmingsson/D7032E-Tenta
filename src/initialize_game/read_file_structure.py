# default
import os


def get_dir_in_path(path: str) -> list:
    """
    This returns a list of the names of the folders in "data" folder.
    These are the game types one can play.
    """
    directories = []
    for _, dirs, _ in os.walk(path):
        directories = dirs
        break

    return directories
