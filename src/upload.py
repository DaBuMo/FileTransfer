from lib.upload import arguments
from lib.upload.Upload import Upload


def upload():
    client = Upload()
    client.start()


if __name__ == "__main__":
    args = arguments.parser.parse_args()

    upload()
