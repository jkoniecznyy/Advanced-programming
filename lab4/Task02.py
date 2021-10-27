# Task 2
from lab4.Task01 import Student


class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self) -> str:
        return f'Ksiegarnia: {self.street} {self.zip_code} {self.city}, godziny {self.open_hours}, nr {self.phone}'


class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date: str, birth_date: str, city: str, street: str,
                 zip_code: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self) -> str:
        return f'Pracownik: {self.first_name} {self.last_name}, zatrudniony {self.hire_date},  urodzony {self.birth_date}, ' \
               f'nr {self.phone}, adres {self.street} {self.zip_code} {self.city}'


class Book:
    def __init__(self, library: Library, publication_date: str, author_name: str, author_surname: str,
                 number_of_pages: int):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self) -> str:
        return f'Ksiazka: {self.publication_date}, {self.author_name} {self.author_surname}, ' \
               f'{self.number_of_pages} stron, z {self.library}'


class Order:
    def __init__(self, employee: Employee, student: Student, books: list, order_date: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self) -> str:
        return f'Zamowienie: \n ' \
               f'{self.employee}, \n ' \
               f'{self.student}, \n' \
               f' Ksiazki: \n ' + ', \n '.join(str(book) for book in self.books) + ', \n' \
               f' Data zamowienia: {self.order_date}'
