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
