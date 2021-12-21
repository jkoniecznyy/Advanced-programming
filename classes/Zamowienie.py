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
    def kupujacy(self) -> str:
        return self._kupujacy

    @kupujacy.setter
    def kupujacy(self, kupujacy: str):
        self._kupujacy = kupujacy

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
               f'kupujacy: \n{self._kupujacy}\n\n' \
               f'lista_nieruchomosci:\n' + \
               '\n'.join(str(nier) for nier in self._lista_nieruchomosci)

    def oblicz_wartosc_zamowienia(self) -> float:
        return round(sum(nieruchomosc.wartosc
                         for nieruchomosc in self._lista_nieruchomosci), 2)

    def oblicz_powierzchnie_zamowienia(self) -> float:
        return round(sum(nieruchomosc.powierzchnia
                         for nieruchomosc in self._lista_nieruchomosci), 2)
