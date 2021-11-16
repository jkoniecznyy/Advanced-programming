class Firma:
    def __init__(self, nazwa: str, adres: str, prezes: str,
                 nip: int, wartoscRynkowa: float) -> None:
        self._nazwa = nazwa
        self._adres = adres
        self._prezes = prezes
        self._nip = nip
        self._wartoscRynkowa = wartoscRynkowa

    @property
    def nazwa(self) -> str:
        return self._nazwa

    @property
    def adres(self) -> str:
        return self._adres

    @property
    def prezes(self) -> str:
        return self._prezes

    @property
    def nip(self) -> int:
        return self._nip

    @property
    def wartoscRynkowa(self) -> float:
        return self._wartoscRynkowa

    def __str__(self) -> str:
        return f'Firma - nazwa {self._nazwa}, ' \
               f'adres {self._adres}, ' \
               f'prezes {self._prezes}, nip {self._nip}, ' \
               f'wartosc rynkowa {self._wartoscRynkowa}'


class FirmaTransportowa(Firma):
    def __init__(self, nazwa: str, adres: str, prezes: str,
                 nip: int, wartoscRynkowa: float) -> None:
        super().__init__(nazwa, adres, prezes, nip, wartoscRynkowa)
        self._typFirmy = 'Transportowa'

    @property
    def typFirmy(self) -> str:
        return self._typFirmy

    def __str__(self) -> str:
        return 'Transportowa ' + super().__str__()


class FirmaSpozywcza(Firma):
    def __init__(self, nazwa: str, adres: str, prezes: str,
                 nip: int, wartoscRynkowa: float) -> None:
        super().__init__(nazwa, adres, prezes, nip, wartoscRynkowa)
        self._typFirmy = 'Spozywcza'

    @property
    def typFirmy(self) -> str:
        return self._typFirmy

    def __str__(self) -> str:
        return 'Spozywcza ' + super().__str__()


class Pojazd:
    def __init__(self, marka: str, model: str, przebieg: int,
                 rokProdukcji: int, pojemnosc: float) -> None:
        self._marka = marka
        self._model = model
        self._przebieg = przebieg
        self._rokProdukcji = rokProdukcji
        self._pojemnosc = pojemnosc

    @property
    def marka(self) -> str:
        return self._marka

    @property
    def model(self) -> str:
        return self._model

    @property
    def przebieg(self) -> int:
        return self._przebieg

    @property
    def rokProdukcji(self) -> int:
        return self._rokProdukcji

    @property
    def pojemnosc(self) -> float:
        return self.pojemnosc

    def __str__(self) -> str:
        return f'Pojazd - marka {self._marka}, ' \
               f'model {self._model}, ' \
               f'przebieg {self._przebieg}, ' \
               f'rok produkcji {self._rokProdukcji}, ' \
               f'pojemnosc {self._pojemnosc}'


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


class Kurs:
    def __init__(self):
        pass

    def __str__(self) -> str:
        return f'Nr kursu {self._numerKursu}, \n' \
               f'Przypisany Pojazd {self._pojazd}, \n' \
               f'FirmaTransportowa {self._firmaTransportowa}, \n' \
               f'CzasRozpoczecia {self._czasRozpoczecia}, \n' \
               f'CzasZakonczenia {self._czasZakonczenia} \n\n' \
               f'Lista odcinkow \n' + \
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


volvo = Pojazd('Volvo', 'Model', 100000, 2018, 2000.00)
# print(volvo)

f1 = FirmaTransportowa('DPF', 'Uniczowska 5', 'Janusz Tracz',
                       1232423423, 400000.5)
# print(f1)

odcinek1 = Odcinek(volvo, 'And Bar', 50, '12', '13')
odcinek2 = Odcinek(volvo, 'And Bar', 60, '12', '13')
odcinek3 = Odcinek(volvo, 'And Bar', 70, '12', '13')
odcinek4 = Odcinek(volvo, 'And Bar', 80, '12', '13')
odcinek5 = Odcinek(volvo, 'And Bar', 90, '12', '13')
# print([odcinek1, odcinek2, odcinek3, odcinek4,
#                        odcinek5])

kurs1 = Kurs()
kurs1.pojazd = volvo
kurs1.numerKursu = 1
kurs1.czasZakonczenia = '10:50'
kurs1.czasRozpoczecia = '6:00'
kurs1.listaOdcinkow = [odcinek1, odcinek2, odcinek3, odcinek4,
                       odcinek5]
kurs1.firmaTransportowa = f1

print(kurs1)
