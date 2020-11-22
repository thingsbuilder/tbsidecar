import os


class Settings:

    def __init__(self):
        self.GRPC_PORT = int(os.environ.get('SIDECAR_GRPC_PORT'))
