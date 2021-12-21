from classes.Nieruchomosc import Nieruchomosc
from classes.Developer import Developer

class Dom(Nieruchomosc):
    def __init__(self, id: int, developer: Developer, powierzchnia: float,
                 wartosc: float, rozmiar_dzialki: float):

        super().__init__(id, developer, powierzchnia, wartosc)
        self._rozmiar_dzialki = rozmiar_dzialki

    @property
    def rozmiar_dzialki(self) -> float:
        return self._rozmiar_dzialki

    @rozmiar_dzialki.setter
    def rozmiar_dzialki(self, rozmiar_dzialki: float):
        self._rozmiar_dzialki = rozmiar_dzialki

    def __str__(self) -> str:
        return super().__str__() + \
               f'rozmiar_dzialki: {self._rozmiar_dzialki}.\n'
