from initialize_game import ContextLoader


def create_game_from_context(context: ContextLoader):
    packet_path = context.packet_path.split("/")[2:]
    import_from = ".".join(packet_path)
    mod = __import__(import_from)
    obj = getattr(mod, context.class_name)(context.all_players, context.deck)
    return obj
