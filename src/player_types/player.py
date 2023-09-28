from abc import ABC, abstractmethod
import socket

from data_structures import ClientConnectionInfo


class Player(ABC):
    def __init__(self) -> None:
        self._score = 0

    @abstractmethod
    def send_message(self, message: str) -> None:
        pass

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @property
    def socket_obj(self) -> socket.socket:
        return self._socket

    @socket_obj.setter
    def socket_obj(self, value: socket.socket) -> None:
        self._socket = value

    @property
    def score(self) -> int:
        return self._score

    def add_score(self, value: int) -> None:
        self._score += value

    @classmethod
    def from_client_connection_info(cls, connection_info: ClientConnectionInfo) -> "Player":
        c = cls()
        c.id = connection_info.id
        return c

    @classmethod
    def from_id(cls, id: int) -> "Player":
        c = cls()
        c.id = id
        return c
