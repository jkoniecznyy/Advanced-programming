from classes.Pojazd import Pojazd
from classes.Odcinek import Odcinek
from classes.FirmaTransportowa import FirmaTransportowa


class Kurs:
    def __init__(self):
        pass

    def __str__(self) -> str:
        return f'Nr kursu {self._numerKursu}, \n' \
               f'Przypisany Pojazd - {self._pojazd}, \n' \
               f'FirmaTransportowa - {self._firmaTransportowa}, \n' \
               f'CzasRozpoczecia - {self._czasRozpoczecia}, \n' \
               f'CzasZakonczenia - {self._czasZakonczenia} \n' \
               f'Lista odcinkow :\n' + \
               ', \n'.join(str(odc) for odc in self.listaOdcinkow)

    @property
    def numerKursu(self) -> int:
        return self._numerKursu

    @numerKursu.setter
    def numerKursu(self, numerKursu: int):
        self._numerKursu = numerKursu

    @property
    def pojazd(self) -> Pojazd:
        return self._pojazd

    @pojazd.setter
    def pojazd(self, pojazd: Pojazd):
        self._pojazd = pojazd

    @property
    def listaOdcinkow(self) -> list:
        return self._listaOdcinkow

    @listaOdcinkow.setter
    def listaOdcinkow(self, listaOdcinkow: list):
        self._listaOdcinkow = listaOdcinkow

    @property
    def firmaTransportowa(self) -> FirmaTransportowa:
        return self._firmaTransportowa

    @firmaTransportowa.setter
    def firmaTransportowa(self, firmaTransportowa: FirmaTransportowa):
        self._firmaTransportowa = firmaTransportowa

    @property
    def czasRozpoczecia(self) -> str:
        return self._czasRozpoczecia

    @czasRozpoczecia.setter
    def czasRozpoczecia(self, czasRozpoczecia: str):
        self._czasRozpoczecia = czasRozpoczecia

    @property
    def czasZakonczenia(self) -> str:
        return self._czasZakonczenia

    @czasZakonczenia.setter
    def czasZakonczenia(self, czasZakonczenia: str):
        self._czasZakonczenia = czasZakonczenia

    def policzKM(self):
        sumaKM = 0
        for odcinek in self._listaOdcinkow:
            sumaKM += odcinek.dlugosc
        return round(sumaKM, 2)

    def markaPojazdu(self):
        return self._pojazd.marka
