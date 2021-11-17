from classes.Pojazd import Pojazd


class Odcinek:
    def __init__(self, przypisanyPojazd: Pojazd, przypisanyKierowca: str,
                 dlugosc: float, czasRozpoczecia: str,
                 czasZakonczenia: str) -> None:
        self._przypisanyPojazd = przypisanyPojazd
        self._przypisanyKierowca = przypisanyKierowca
        self._dlugosc = dlugosc
        self._czasRozpoczecia = czasRozpoczecia
        self._czasZakonczenia = czasZakonczenia

    @property
    def przypisanyPojazd(self) -> Pojazd:
        return self._przypisanyPojazd

    @property
    def przypisanyKierowca(self) -> str:
        return self._przypisanyKierowca

    @property
    def dlugosc(self) -> float:
        return self._dlugosc

    @property
    def czasRozpoczecia(self) -> str:
        return self._czasRozpoczecia

    @property
    def czasZakonczenia(self) -> str:
        return self.czasZakonczenia

    def __str__(self) -> str:
        return f'Odcinek - przypisany Pojazd {self._przypisanyPojazd}, ' \
               f'przypisanyKierowca {self._przypisanyKierowca}, ' \
               f'dlugosc {self._dlugosc}, ' \
               f'czasRozpoczecia {self._czasRozpoczecia}, ' \
               f'czasZakonczenia {self._czasZakonczenia}'
