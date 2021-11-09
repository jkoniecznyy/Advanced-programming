class Firma:
    def __init__(self, nazwa: str, adres: str, prezes: str,
                 nip: int, wartoscRynkowa: float) -> None:
        self.__nazwa = nazwa
        self.__adres = adres
        self.__prezes = prezes
        self.__nip = nip
        self.__wartoscRynkowa = wartoscRynkowa

    @property
    def nazwa(self) -> str:
        return self.__nazwa

    @property
    def adres(self) -> str:
        return self.__adres

    @property
    def prezes(self) -> str:
        return self.__prezes

    @property
    def nip(self) -> int:
        return self.__nip

    @property
    def wartoscRynkowa(self) -> float:
        return self.__wartoscRynkowa

    def __str__(self) -> str:
        return f'Firma o nazwie {self.__nazwa}, ' \
               f'adresie {self.__adres},' \
               f' prezes {self.__prezes}, nip {self.__nip},' \
               f' wartosc rynkowa {self.__wartoscRynkowa}'


class FirmaTransportowa(Firma):
    def __init__(self, nazwa: str, adres: str, prezes: str,
                 nip: int, wartoscRynkowa: float) -> None:
        super().__init__(nazwa, adres, prezes, nip, wartoscRynkowa)
        self.__typFirmy = 'Transportowa'

    @property
    def typFirmy(self) -> str:
        return self.__typFirmy

    def __str__(self) -> str:
        return 'Transportowa ' + super().__str__()


class FirmaSpozywcza(Firma):
    def __init__(self, nazwa: str, adres: str, prezes: str,
                 nip: int, wartoscRynkowa: float) -> None:
        super().__init__(nazwa, adres, prezes, nip, wartoscRynkowa)
        self.__typFirmy = 'Spozywcza'

    @property
    def typFirmy(self) -> str:
        return self.__typFirmy

    def __str__(self) -> str:
        return 'Spozywcza ' + super().__str__()


class Pojazd:
    def __init__(self, marka: str, model: str, przebieg: int, rokProdukcji: int, pojemnosc: float) -> None:
        self.__marka = marka
        self.__model = model
        self.__przebieg = przebieg
        self.__rokProdukcji = rokProdukcji
        self.__pojemnosc = pojemnosc

    @property
    def marka(self) -> str:
        return self.__marka

    @property
    def model(self) -> str:
        return self.__model

    @property
    def przebieg(self) -> int:
        return self.__przebieg

    @property
    def rokProdukcji(self) -> int:
        return self.__rokProdukcji

    @property
    def pojemnosc(self) -> float:
        return self.pojemnosc

    def __str__(self) -> str:
        return f'Pojazd o marce {self.__marka}, ' \
               f'modelu {self.__model},' \
               f' przebiegu {self.__przebieg}, ' \
               f'roku Produkcji {self.__rokProdukcji},' \
               f' pojemnosci {self.__pojemnosc}'


class Odcinek:
    def __init__(self, przypisanyPojazd: Pojazd, przypisanyKierowca: str, dlugosc: float, czasRozpoczecia: str,
                 czasZakonczenia: str) -> None:
        self.__przypisanyPojazd = przypisanyPojazd
        self.__przypisanyKierowca = przypisanyKierowca
        self.__dlugosc = dlugosc
        self.__czasRozpoczecia = czasRozpoczecia
        self.__czasZakonczenia = czasZakonczenia

    @property
    def przypisanyPojazd(self) -> Pojazd:
        return self.__przypisanyPojazd

    @property
    def przypisanyKierowca(self) -> str:
        return self.__przypisanyKierowca

    @property
    def dlugosc(self) -> float:
        return self.__dlugosc

    @property
    def czasRozpoczecia(self) -> str:
        return self.__czasRozpoczecia

    @property
    def czasZakonczenia(self) -> str:
        return self.czasZakonczenia

    def __str__(self) -> str:
        return f'Odcinek przypisany Pojazd{self.__przypisanyPojazd}, ' \
               f'przypisanyKierowca {self.__przypisanyKierowca},' \
               f' dlugosc {self.__dlugosc}, ' \
               f'czasRozpoczecia {self.__czasRozpoczecia},' \
               f' czasZakonczenia {self.__czasZakonczenia}'


class Kurs:
    def __init__(self) -> None:
        self.__numerKursu = 0
        self.__pojazd = Pojazd
        self.__listaOdcinkow = []
        self.__firmaTransportowa = FirmaTransportowa
        self.__czasRozpoczecia = ''
        self.__czasZakonczenia = ''


    @property
    def get_numerKursu(self) -> int:
        return self.__numerKursu

    @property
    def get_pojazd(self) -> Type[Pojazd]:
        return self.__pojazd

    @property
    def get_listaOdcinkow(self) -> list:
        return self.__listaOdcinkow

    @property
    def get_firmaTransportowa(self) -> Type[FirmaTransportowa]:
        return self.__firmaTransportowa

    @property
    def get_czasRozpoczecia(self) -> str:
        return self.__czasRozpoczecia

    @property
    def get_czasZakonczenia(self) -> str:
        return self.czasZakonczenia

    @numerKursu.setter
    def numerKursu(self, value: int) -> None:
        self.__numerKursu = value

    @pojazd.setter
    def pojazd(self, value: Pojazd) -> None:
        self.__pojazd = value

    @listaOdcinkow.setter
    def listaOdcinkow(self, value: list) -> None:
        self.__listaOdcinkow = value

    @firmaTransportowa.setter
    def firmaTransportowa(self, value: FirmaTransportowa) -> None:
        self.__firmaTransportowa = value

    @czasRozpoczecia.setter
    def czasRozpoczecia(self, value: str) -> None:
        self.__numerKursu = value

    @czasZakonczenia.setter
    def czasZakonczenia(self, value: str) -> None:
        self.__czasRozpoczecia = value

    def __str__(self) -> str:
        return f'Odcinek przypisany Pojazd{self.__przypisanyPojazd}, ' \
               f'przypisanyKierowca {self.__przypisanyKierowca},' \
               f' dlugosc {self.__dlugosc}, ' \
               f'czasRozpoczecia {self.__czasRozpoczecia},' \
               f' czasZakonczenia {self.__czasZakonczenia}'

    def policzKM(self):
        sumaKM = 0
        for odcinek in self.__listaOdcinkow:
            sumaKM += odcinek.dlugosc
        return round(sumaKM, 2)

    def markaPojazdu(self):
        return self.__pojazd.marka



# self.__numerKursu = 0
#         self.__pojazd = Pojazd
#         self.__listaOdcinkow = []
#         self.__firmaTransportowa = FirmaTransportowa
#         self.__czasRozpoczecia = ''
#         self.__czasZakonczenia = ''
# (self, marka: str, model: str, przebieg: int, rokProdukcji: int, pojemnosc: float)
volvo = Pojazd('Volvo', 'Model', 100000, 2018, 2000.00)
print(volvo)


# (self, nazwa: str, adres: str, prezes: str,
#              nip: int, wartoscRynkowa: float):
f1 = FirmaTransportowa('DPF', 'Uniczowska 5', 'Janusz Tracz', 1232423423, 400000.5)
print(f1)

# def __init__(self, przypisanyPojazd: Pojazd, przypisanyKierowca: str, dlugosc: float, czasRozpoczecia: str,
#                  czasZakonczenia: str) -> None:
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
kurs1.listaOdcinkow([odcinek1,odcinek2, odcinek3, odcinek4, odcinek6])





