from classes.Developer import Developer


class Nieruchomosc:
    def __init__(self, id: int, developer: Developer,
                 powierzchnia: float, wartosc: float):
        self._id = id
        self._developer = developer
        self._powierzchnia = powierzchnia
        self._wartosc = wartosc

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def developer(self) -> Developer:
        return self._developer

    @developer.setter
    def developer(self, developer: Developer):
        self._developer = developer

    @property
    def powierzchnia(self) -> float:
        return self._powierzchnia

    @powierzchnia.setter
    def powierzchnia(self, powierzchnia: float):
        self._powierzchnia = powierzchnia

    @property
    def wartosc(self) -> float:
        return self._wartosc

    @wartosc.setter
    def wartosc(self, wartosc: float):
        self._wartosc = wartosc

    def __str__(self) -> str:
        return f'id: {self._id},\n' \
               f'developer: {self._developer},\n' \
               f'powierzchnia: {self._powierzchnia},\n' \
               f'wartosc: {self._wartosc}.\n'
