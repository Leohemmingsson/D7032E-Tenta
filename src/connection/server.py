import asyncio
import socket
from data_structures import ClientConnectionInfo
from .utils import get_full_message, send_message_to


class Server:
    def __init__(self, PORT: int | None = None, HEADERSIZE: int | None = None) -> None:
        if PORT is None:
            PORT = 1234
        self.PORT = PORT
        self.HEADERSIZE = HEADERSIZE
        self.greeting_message = "Connected to the server!"
        self.s: socket.socket

    def start_server(self, number_of_clients: int) -> list[ClientConnectionInfo] | None:
        """
        Starts a tcp server on given port, default port=1234
        """
        if number_of_clients < 1:
            return None

        try:
            connection_info = self._connect_to_socket(number_of_clients)
            return connection_info
        except OSError:
            print("Port already in use. Try again.")

    def get_answers_from_clients(self, client_info: list[ClientConnectionInfo]) -> list[tuple]:
        """
        Waits for all clients to send a message, and returns a list of tuples
        """
        answer = []
        for client in client_info:
            message = asyncio.run(self._listen_to_client(client.socket_connection))
            answer.append((client.id, message))
        return answer

    async def _listen_to_client(self, s_client: socket.socket) -> str:
        message = get_full_message(s_client, self.HEADERSIZE)
        return message

    def _connect_to_socket(self, number_of_clients):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((socket.gethostname(), self.PORT))
        s.listen(5)
        self.s = s
        print(f"Server is listening on port {self.PORT}...")

        client_info = self._get_all_clients_connection_info(s, number_of_clients)
        print("All clients connected!")
        return client_info

    def _get_all_clients_connection_info(self, s: socket.socket, number_of_clients: int) -> list[ClientConnectionInfo]:
        print(f"Waiting for {number_of_clients} clients to connect...")
        all_clients = []

        for i in range(number_of_clients):
            s_client, address = s.accept()
            id = i + 1
            all_clients.append(
                ClientConnectionInfo(
                    id=id,
                    socket_connection=s_client,
                    address=address,
                )
            )
            print(f"Connection from {address} has been established!")
            send_message_to(s_client, self.greeting_message)

        return all_clients

    def close_server(self) -> None:
        self.s.close()
