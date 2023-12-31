import yaml


class PackageData:
    """
    This is the structure to get all data from a packages config file.
    """

    def __init__(self, path) -> None:
        self._deck_filename = path + "/cards.csv"
        self._load_data_from_config(path + "/config.yml")
        self._path = path

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

    @property
    def card_class_name(self) -> str:
        return self._card_class_name

    @property
    def path(self) -> str:
        return self._path

    def _load_data_from_config(self, path: str) -> None:
        with open(path, "r") as file:
            config_values = yaml.safe_load(file)
        self._name = config_values["about"]["name"]
        self._class_name = config_values["about"]["class_name"]
        self._card_class_name = config_values["about"]["card_class_name"]
        self._is_active = bool(config_values["about"]["is_active"])
