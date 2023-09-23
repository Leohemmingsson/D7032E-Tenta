from abc import ABC, abstractmethod

from data_structures import ClientConnectionInfo


class Player(ABC):
    def __init__(self, connection_info: ClientConnectionInfo) -> None:
        self._id = connection_info.id
        self._socket = connection_info.socket_connection
        self._score = 0

    @abstractmethod
    def send_message(self, message: str) -> None:
        pass

    @property
    def id(self) -> int:
        return self._id
