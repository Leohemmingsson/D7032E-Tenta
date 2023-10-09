# std
import os
from subprocess import call
import socket

# own
from .utils import get_full_message, send_message_to


class Client:
    def __init__(self, PORT: int | None = None, HEADERSIZE: int | None = None) -> None:
        if PORT is None:
            PORT = 1234
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

    def _listen_to_server(self, s: socket.socket) -> str:
        message = get_full_message(s, self.HEADERSIZE)
        return message

    def _output_formatted_response(self, response: str) -> None:
        print(response)

    def _connect_to_server(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((socket.gethostname(), self.PORT))

        while True:
            response = self._listen_to_server(s)
            self._output_formatted_response(response)
            if "Choose" in response:
                user_input = input()
                send_message_to(s, user_input)
            elif response == "clear":
                _ = call("clear" if os.name == "posix" else "cls")


if __name__ == "__main__":
    client = Client()
    client.run_client()
