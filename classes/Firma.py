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
