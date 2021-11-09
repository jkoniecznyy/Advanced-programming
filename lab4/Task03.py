# Task 3
class Property:
    def __init__(self, area: int, rooms: int, price: float, address: str):
        self._area = area
        self._rooms = rooms
        self._price = price
        self._address = address

    def __str__(self) -> str:
        return f'Dane nieruchomości: powierzchnia - {self._area},' \
               f' pokoje - {self._rooms}, ' \
               f'cena - {self._price}, adres - {self._address}'


class House(Property):
    def __init__(self, area: int, rooms: int, price: float,
                 address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self._plot = plot

    def __str__(self) -> str:
        return 'Dom: ' + super().__str__() + f', rozmiar dzialki - {self._plot}'


class Flat(Property):
    def __init__(self, area: int, rooms: int, price: float,
                 address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self._floor = floor

    def __str__(self) -> str:
        return 'Mieszkanie: ' + super().__str__() + f', piętro - {self._floor}'
