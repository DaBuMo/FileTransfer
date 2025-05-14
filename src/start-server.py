from lib.server import arguments
from lib.server.Server import Server


def start_server(host: str, port: int):
    server = Server(port, host)
    server.start()


if __name__ == "__main__":
    # read host and port from command line arguments
    args = arguments.parser.parse_args()
    host = args.host
    port = args.port
    # start server
    start_server(host, port)
