import socket
from dataclasses import dataclass


@dataclass
class ClientConnectionInfo:
    id: int
    socket_connection: socket.socket
    address: tuple[str, int] | None
