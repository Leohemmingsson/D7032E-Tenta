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
    directories = _remove_settings_dir(directories)

    return directories


def _remove_settings_dir(paths: list):
    for one_path in paths:
        if one_path.startswith("__"):
            paths.remove(one_path)
    return paths
