from magazine.utils import clients


class Order:
    def __init__(self):
        self._clients = clients

    def showClients(self) -> str:
        return self._clients
