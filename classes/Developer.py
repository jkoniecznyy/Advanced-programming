class Developer:
    def __init__(self, imie: str, nazwisko: str, telefon: int, email: str):
        self._email = email
        self._telefon = telefon
        self._nazwisko = nazwisko
        self._imie = imie

    @property
    def imie(self) -> str:
        return self._imie

    @imie.setter
    def imie(self, imie: str):
        self._imie = imie

    @property
    def nazwisko(self) -> str:
        return self._nazwisko

    @nazwisko.setter
    def nazwisko(self, nazwisko: str):
        self._nazwisko = nazwisko

    @property
    def telefon(self) -> int:
        return self._telefon

    @telefon.setter
    def telefon(self, telefon: int):
        self._telefon = telefon

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str):
        self._email = email

    def __str__(self) -> str:
        return f'imie: {self._imie}, ' \
               f'nazwisko: {self._nazwisko}, ' \
               f'telefon: {self._telefon}, ' \
               f'email: {self._email}.'
