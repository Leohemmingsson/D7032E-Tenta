import socket


def run_client(PORT: str | None = "1234", HEADERSIZE: int = 10):
    """
    Connect client to server.
    Args:
        port (str): Port number to connect to. Defaults to "1234".
        headersize (int): Size of the header. Defaults to 10.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1234))

    while True:
        response = _listen_to_server(s, HEADERSIZE)
        _output_formatted_response(response)


def _listen_to_server(s: socket.socket, HEADERSIZE: int):
    full_message = ""
    while True:
        message = s.recv(16)
        message_length = int(message[:HEADERSIZE])

        full_message += message.decode("utf-8")

        if len(full_message) - HEADERSIZE == message_length:
            return full_message[HEADERSIZE:]


def _output_formatted_response(response: str):
    print(response)
