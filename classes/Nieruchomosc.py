class Nieruchomosc:
    def __init__(self, id: int, miasto: str,
                 powierzchnia: float, wartosc: float):
        self._id = id
        self._miasto = miasto
        self._powierzchnia = powierzchnia
        self._wartosc = wartosc

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def miasto(self) -> str:
        return self._miasto

    @miasto.setter
    def miasto(self, miasto: str):
        self._miasto = miasto

    @property
    def powierzchnia(self) -> float:
        return self._powierzchnia

    @powierzchnia.setter
    def powierzchnia(self, powierzchnia: float):
        self._powierzchnia = powierzchnia

    @property
    def wartosc(self) -> float:
        return self._wartosc

    @wartosc.setter
    def wartosc(self, wartosc: float):
        self._wartosc = wartosc

    def __str__(self) -> str:
        return f'id: {self._id},\n' \
               f'miasto: {self._miasto},\n' \
               f'powierzchnia: {self._powierzchnia},\n' \
               f'wartosc: {self._wartosc}.\n'
