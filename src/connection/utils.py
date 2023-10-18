# std
import json
import socket

# own
from ..data_structures import ClientConnectionInfo


def get_full_message(s, HEADERSIZE: int | None = None) -> dict:
    if HEADERSIZE is None:
        HEADERSIZE = 10

    full_message = ""
    new_message = True
    message_length: int = 0
    to_receive = 10
    current_length = 0
    while True:
        if not new_message and (message_length - current_length) < to_receive:
            to_receive = message_length - current_length
        message = s.recv(to_receive)
        if len(message) == 0:
            print("Connection closed")
            exit()

        if new_message:
            message_length = int(message[:HEADERSIZE])
            new_message = False

        try:
            full_message += message.decode("utf-8")
        except UnicodeDecodeError:
            print("UnicodeDecodeError")
            print(message)
            exit()

        current_length = len(full_message) - HEADERSIZE
        if current_length == message_length:
            return json.loads(full_message[HEADERSIZE:])


def broadcast_message_to(all_clients_connection_info: list[ClientConnectionInfo], message: str) -> None:
    for client in all_clients_connection_info:
        if client.socket_connection is not None:
            send_message_to(client.socket_connection, message)


def send_message_to(s: socket.socket, message: str, is_question: bool = False, special: bool = False) -> None:
    wrapped_message = {"message": message, "is_question": is_question, "special": special}
    s.send(bytes(_prefix_message(json.dumps(wrapped_message)), "utf-8"))


def _prefix_message(message, HEADERSIZE: int | None = None) -> str:
    if HEADERSIZE is None:
        HEADERSIZE = 10
    prefixed_message = f"{len(message):<{HEADERSIZE}}{message}"
    return prefixed_message
