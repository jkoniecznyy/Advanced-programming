from classes.Firma import Firma


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
