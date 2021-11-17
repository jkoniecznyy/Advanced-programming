from classes.Pojazd import Pojazd
from classes.Odcinek import Odcinek
from classes.FirmaTransportowa import FirmaTransportowa
from classes.FirmaSpozywcza import FirmaSpozywcza
from classes.Kurs import Kurs

volvo = Pojazd('Volvo', 'Model', 100000, 2018, 2000.00)
# print(volvo)

f1 = FirmaTransportowa('DPF', 'Uniczowska 5', 'Janusz Tracz',
                       1232423423, 400000.5)
# print(f1)

odcinek1 = Odcinek(volvo, 'And Bar', 50, '12', '13')
odcinek2 = Odcinek(volvo, 'And Bar', 60, '12', '13')
odcinek3 = Odcinek(volvo, 'And Bar', 70, '12', '13')
odcinek4 = Odcinek(volvo, 'And Bar', 80, '12', '13')
odcinek5 = Odcinek(volvo, 'And Bar', 90, '12', '13')
# print([odcinek1, odcinek2, odcinek3, odcinek4,
#                        odcinek5])

kurs1 = Kurs()
kurs1.pojazd = volvo
kurs1.numerKursu = 1
kurs1.czasZakonczenia = '10:50'
kurs1.czasRozpoczecia = '6:00'
kurs1.listaOdcinkow = [odcinek1, odcinek2, odcinek3, odcinek4,
                       odcinek5]
kurs1.firmaTransportowa = f1

print(kurs1)
