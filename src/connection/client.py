# std
import os
from subprocess import call
import socket

# own
from .utils import get_full_message, send_message_to


class Client:
    def __init__(self, PORT: int | None = None, IP: str | None = None, HEADERSIZE: int | None = None) -> None:
        if PORT is None:
            PORT = 1234
        if IP is None:
            IP = socket.gethostname()
        self.IP = IP
        self.PORT = PORT
        self.HEADERSIZE = HEADERSIZE

    def run_client(self) -> None:
        """
        Connect client to server, and act as a monitor from server
        """
        try:
            self._connect_to_server()
        except ConnectionRefusedError:
            print(f"Connection refused. Make sure the server is running on port {self.PORT}")

    def _listen_to_server(self, s: socket.socket) -> dict:
        message = get_full_message(s, self.HEADERSIZE)
        return message

    def _connect_to_server(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.IP, self.PORT))

        while True:
            response = self._listen_to_server(s)
            print(response["message"])
            if response["is_question"]:
                user_input = input()
                send_message_to(s, user_input)
            elif response["special"]:
                if response["message"] == "clear":
                    call("clear" if os.name == "posix" else "cls")


if __name__ == "__main__":
    client = Client()
    client.run_client()
