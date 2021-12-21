from classes.Nieruchomosc import Nieruchomosc
from classes.Mieszkanie import Mieszkanie
from classes.Dom import Dom
from classes.Developer import Developer
from classes.Zamowienie import Zamowienie


dev1 = Developer('Janusz', 'Tracz', 513333555, 'jantracz@gmail.com')
nier1 = Nieruchomosc(1, 'Krakow', 70.21231, 300000)
dom1 = Dom(2, 'Wroclaw', 90.5, 1000000.99999999, 100.54564)
miesz1 = Mieszkanie(3, 'Warszawa', 20.0786, 200000, 3)

zam1 = Zamowienie()
zam1.id = 1
zam1.data = '21.12.2021'
zam1.developer = dev1
zam1.lista_nieruchomosci = [nier1, dom1, miesz1]
print(zam1)
print('Laczna wartosc:', zam1.oblicz_wartosc_zamowienia())
print('Laczna powierzchnia:', zam1.oblicz_powierzchnie_zamowienia())
