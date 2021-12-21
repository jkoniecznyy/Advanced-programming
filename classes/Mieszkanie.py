from classes.Nieruchomosc import Nieruchomosc


class Mieszkanie(Nieruchomosc):
    def __init__(self, id: int, miasto: str, powierzchnia: float,
                 wartosc: float, pietro: int):
        super().__init__(id, miasto, powierzchnia, wartosc)
        self._pietro = pietro

    @property
    def pietro(self) -> int:
        return self._pietro

    @pietro.setter
    def pietro(self, pietro: int):
        self._pietro = pietro

    def __str__(self) -> str:
        return super().__str__() + f'pietro: {self._pietro}.\n'
