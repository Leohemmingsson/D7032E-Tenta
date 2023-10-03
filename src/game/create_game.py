from . import boomerang
from .boomerang import Boomerang
from initialize_game import ContextLoader


def create_game_from_context(context: ContextLoader) -> Boomerang:
    """
    Dynamically create a game from the context.
    """

    boomerang_obj = getattr(boomerang, context.class_name)(context.all_players, context.deck)
    return boomerang_obj
