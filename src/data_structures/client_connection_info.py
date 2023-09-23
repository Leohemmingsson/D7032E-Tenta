import socket
from dataclasses import dataclass


@dataclass
class ClientConnectionInfo:
    id: int
    socket_connection: socket.socket | None
    address: tuple[str, int] | None
