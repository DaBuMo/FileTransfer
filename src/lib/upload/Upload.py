import socket

from lib.constants import BUFSIZE, DEFAULT_PORT, LOCALHOST


class Upload:
    def __init__(self):
        pass

    def start(self):
        upload_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        data = b"hello world"
        upload_socket.sendto(data, (LOCALHOST, DEFAULT_PORT))

        received, addr = upload_socket.recvfrom(BUFSIZE)
        print(received, addr)
        upload_socket.close()
