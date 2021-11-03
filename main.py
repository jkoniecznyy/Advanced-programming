from lab4.Task01 import Student
from lab4.Task02 import Library, Employee, Book, Order
from lab4.Task03 import Flat, House

print("\nTask1\n")

stud1 = Student('Andrzej Gołota', 51)
stud2 = Student('Marcin Najman', 50)
stud3 = Student('Mariusz Pudzianowski', 53)
print(stud1.is_passed())
print(stud2.is_passed())

print("\nTask2\n")

lib1 = Library('Mikołów', 'Mysia', '43-190', 'pon-pt 8-12', '+48 123 456 789')
lib2 = Library('Mikołów', 'Reta', '43-190', 'pon-pt 8-16', '+48 444 456 888')
book1 = Book(lib1, '14.02.2001', 'Jerzy', 'Killer', 550)
book2 = Book(lib1, '14.02.2011', 'Krzysztof', 'Waski', 500)
book3 = Book(lib2, '14.03.2021', 'Stefan', 'Siara', 600)
book4 = Book(lib2, '14.04.2021', 'Gabrysia', 'Siarzewska', 2000)
book5 = Book(lib1, '14.05.2021', 'Jerzy', 'Ryba', 60)
emp1 = Employee('Artur', 'Boruc', '23.10.2020', '20.01.1990',
                'Mikołów', 'Krucza', '43-190', '+48 333 456 777')
emp2 = Employee('Wojtek', 'Szczesny', '23.10.2019', '21.01.1990',
                'Mikołów', 'Jana Pawla', '43-190', '+48 333 456 999')
emp3 = Employee('Luki', 'Fabianski', '23.10.2018', '22.01.1990',
                'Mikołów', 'Zachodnia', '43-190', '+48 333 456 000')
order1 = Order(emp1, stud1, [book1, book3, book2], '26.10.2021')
order2 = Order(emp3, stud3, [book3, book4, book5], '27.10.2021')
print(order1)
print()
print(order2)

print("\nTask3\n")

house1 = House(102, 3, 700000, 'Zukowa, Opole', 700)
flat1 = Flat(42, 1, 200000, 'Muzyczna, Krasiejow', 3)
print(house1)
print(flat1)
