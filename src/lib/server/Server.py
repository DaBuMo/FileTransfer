from socket import AF_INET, SOCK_DGRAM, socket

BUFSIZE = 1024


class Server:
    def __init__(self, port: int, host: int):
        self.port = port
        self.host = host
        self.running = False

    def start(self):
        server_socket = socket(AF_INET, SOCK_DGRAM)
        server_socket.bind((self.host, self.port))
        self.running = True
        print(f"Starting server on {self.host}:{self.port}")

        while self.running:
            data, client_addr = server_socket.recvfrom(BUFSIZE)
            print(f"Received data: {data} from {client_addr}")
            server_socket.sendto(data.upper(), client_addr)
            print(f"Sent data: {data.upper()} to {client_addr}")

        server_socket.close()
        print("Server closed")
