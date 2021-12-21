from classes.Developer import Developer
from classes.Nieruchomosc import Nieruchomosc


class Zamowienie:
    def __init__(self):
        pass

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def data(self) -> str:
        return self._data

    @data.setter
    def data(self, data: str):
        self._data = data

    @property
    def developer(self) -> Developer:
        return self._developer

    @developer.setter
    def developer(self, developer: Developer):
        self._developer = developer

    @property
    def lista_nieruchomosci(self) -> list[Nieruchomosc]:
        return self._lista_nieruchomosci

    @lista_nieruchomosci.setter
    def lista_nieruchomosci(self, lista_nieruchomosci: list[Nieruchomosc]):
        self._lista_nieruchomosci = lista_nieruchomosci

    def __str__(self) -> str:
        return f'Zamowienie:\n' \
               f'id: {self._id},\n' \
               f'data: {self._data},\n' \
               f'developer: \n{self._developer}\n\n' \
               f'lista_nieruchomosci:\n' + \
               '\n'.join(str(nier) for nier in self._lista_nieruchomosci)

    def oblicz_wartosc_zamowienia(self) -> float:
        result = 0
        for nieruchomosc in self._lista_nieruchomosci:
            result += nieruchomosc.wartosc
        return round(result, 2)

    def oblicz_powierzchnie_zamowienia(self) -> float:
        result = 0
        for nieruchomosc in self._lista_nieruchomosci:
            result += nieruchomosc.powierzchnia
        return round(result, 2)
