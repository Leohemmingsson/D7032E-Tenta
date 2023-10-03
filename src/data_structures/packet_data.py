import yaml


class PacketData:
    def __init__(self, path) -> None:
        self._deck_filename = path + "/cards.csv"
        self.load_data_from_config(path + "/config.yml")

    def __repr__(self) -> str:
        return self._name

    @property
    def deck_path(self) -> str:
        return self._deck_filename

    @property
    def is_active(self) -> bool:
        return self._is_active

    @property
    def class_name(self) -> str:
        return self._class_name

    def load_data_from_config(self, path: str) -> None:
        with open(path, "r") as file:
            config_values = yaml.safe_load(file)
        self._name = config_values["about"]["name"]
        self._class_name = config_values["about"]["class_name"]
        self._is_active = bool(config_values["about"]["is_active"])
