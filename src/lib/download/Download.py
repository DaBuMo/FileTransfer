class Download:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    def start(self, filename: str):
        print(filename)
