from initialize_game import ContextLoader
from .boomerang import Boomerang


def create_game_from_context(context: ContextLoader) -> Boomerang:
    """
    Based on the context this function will import the correct game class and return an instance of it.
    The class is declared in a folder inside the data folder. This means when adding a new game, it can be
    imported as long as it is in the correct folder.
    """
    import_from = _make_path_to_import(context.packet_path)
    mod = __import__(import_from)
    boomerang_obj = getattr(mod, context.class_name)(context.all_players, context.deck)
    return boomerang_obj


def _make_path_to_import(path: str) -> str:
    """
    Input in format ./src/data/<foldername>/
    Output in format data.<foldername>
    """
    return ".".join(path.split("/")[2:])
