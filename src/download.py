from lib.download import arguments
from lib.download.Download import Download


def download():
    client = Download()
    client.start()


if __name__ == "__main__":
    args = arguments.parser.parse_args()

    download()
