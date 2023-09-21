import socket
from .client_connection_info import ClientConnectionInfo


def get_full_message(s, HEADERSIZE: int | None = None) -> str:
    if HEADERSIZE is None:
        HEADERSIZE = 10
    full_message = ""
    new_message = True
    message_length: int = 0
    while True:
        message = s.recv(16)
        if len(message) == 0:
            print("Connection closed")
            exit()

        if new_message:
            message_length = int(message[:HEADERSIZE])
            new_message = False

        full_message += message.decode("utf-8")

        if len(full_message) - HEADERSIZE == message_length:
            return full_message[HEADERSIZE:]


def broadcast_message_to(all_clients_connection_info: list[ClientConnectionInfo], message: str) -> None:
    for client in all_clients_connection_info:
        send_message_to(client.socket_connection, message)


def send_message_to(s: socket.socket, message: str) -> None:
    s.send(bytes(_prefix_message(message), "utf-8"))


def _prefix_message(message, HEADERSIZE: int | None = None) -> str:
    if HEADERSIZE is None:
        HEADERSIZE = 10
    prefixed_message = f"{len(message):<{HEADERSIZE}}{message}"
    return prefixed_message
