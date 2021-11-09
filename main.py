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
        return f'Firma o nazwie {self._nazwa}, ' \
               f'adresie {self._adres},' \
               f' prezes {self._prezes}, nip {self._nip},' \
               f' wartosc rynkowa {self._wartoscRynkowa}'


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
    def __init__(self, marka: str, model: str, przebieg: int, rokProdukcji: int, pojemnosc: float) -> None:
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
        return f'Pojazd o marce {self._marka}, ' \
               f'modelu {self._model},' \
               f' przebiegu {self._przebieg}, ' \
               f'roku Produkcji {self._rokProdukcji},' \
               f' pojemnosci {self._pojemnosc}'


class Odcinek:
    def __init__(self, przypisanyPojazd: Pojazd, przypisanyKierowca: str, dlugosc: float, czasRozpoczecia: str,
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
        return f'Odcinek przypisany Pojazd{self._przypisanyPojazd}, ' \
               f'przypisanyKierowca {self._przypisanyKierowca},' \
               f' dlugosc {self._dlugosc}, ' \
               f'czasRozpoczecia {self._czasRozpoczecia},' \
               f' czasZakonczenia {self._czasZakonczenia}'


class Kurs:
    def __init__(self) -> None:
        self._numerKursu = 0
        self._pojazd = Pojazd
        self._listaOdcinkow = []
        self._firmaTransportowa = FirmaTransportowa
        self._czasRozpoczecia = ''
        self._czasZakonczenia = ''

    @property
    def get_numerKursu(self) -> int:
        return self._numerKursu

    @property
    def get_pojazd(self) -> Pojazd:
        return self._pojazd

    @property
    def get_listaOdcinkow(self) -> list:
        return self._listaOdcinkow

    @property
    def get_firmaTransportowa(self) -> FirmaTransportowa:
        return self._firmaTransportowa

    @property
    def get_czasRozpoczecia(self) -> str:
        return self._czasRozpoczecia

    @property
    def get_czasZakonczenia(self) -> str:
        return self._czasZakonczenia

    @numerKursu.setter
    def numerKursu(self, value: int) -> None:
        self._numerKursu = value

    @pojazd.setter
    def pojazd(self, value: Pojazd) -> None:
        self._pojazd = value

    @listaOdcinkow.setter
    def listaOdcinkow(self, value: list) -> None:
        self._listaOdcinkow = value

    @firmaTransportowa.setter
    def firmaTransportowa(self, value: FirmaTransportowa) -> None:
        self._firmaTransportowa = value

    @czasRozpoczecia.setter
    def czasRozpoczecia(self, value: str) -> None:
        self._numerKursu = value

    @czasZakonczenia.setter
    def czasZakonczenia(self, value: str) -> None:
        self._czasRozpoczecia = value

    def __str__(self) -> str:
        return f'Odcinek przypisany Pojazd{self._przypisanyPojazd}, ' \
               f'przypisanyKierowca {self._przypisanyKierowca},' \
               f' dlugosc {self._dlugosc}, ' \
               f'czasRozpoczecia {self._czasRozpoczecia},' \
               f' czasZakonczenia {self._czasZakonczenia}'

    def policzKM(self):
        sumaKM = 0
        for odcinek in self._listaOdcinkow:
            sumaKM += odcinek.dlugosc
        return round(sumaKM, 2)

    def markaPojazdu(self):
        return self._pojazd.marka


volvo = Pojazd('Volvo', 'Model', 100000, 2018, 2000.00)
print(volvo)

f1 = FirmaTransportowa('DPF', 'Uniczowska 5', 'Janusz Tracz', 1232423423, 400000.5)
print(f1)

odcinek1 = Odcinek(volvo, 'And Bar', 50, '12', '13')
odcinek2 = Odcinek(volvo, 'And Bar', 60, '12', '13')
odcinek3 = Odcinek(volvo, 'And Bar', 70, '12', '13')
odcinek4 = Odcinek(volvo, 'And Bar', 80, '12', '13')
odcinek6 = Odcinek(volvo, 'And Bar', 90, '12', '13')
print(odcinek6)

kurs1 = Kurs()
kurs1.pojazd(volvo)
kurs1.numerKursu(1)
kurs1.czasZakonczenia('10')
kurs1.czasRozpoczecia('6')
kurs1.listaOdcinkow([odcinek1, odcinek2, odcinek3, odcinek4, odcinek6])
kurs1.firmaTransportowa(f1)
