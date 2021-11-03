# Task 3
class Property:
    def __init__(self, area: int, rooms: int, price: float, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self) -> str:
        return f'Dane nieruchomości: powierzchnia - {self.area},' \
               f' pokoje - {self.rooms}, ' \
               f'cena - {self.price}, adres - {self.address}'


class House(Property):
    def __init__(self, area: int, rooms: int, price: float,
                 address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self) -> str:
        return 'Dom: ' + super().__str__() + f', rozmiar dzialki - {self.plot}'


class Flat(Property):
    def __init__(self, area: int, rooms: int, price: float,
                 address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self) -> str:
        return 'Mieszkanie: ' + super().__str__() + f', piętro - {self.floor}'
