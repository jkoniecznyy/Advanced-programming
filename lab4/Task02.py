# Task 2
from lab4.Task01 import Student


class Library:
    def __init__(self, city: str, street: str, zip_code: str,
                 open_hours: str, phone: str):
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._open_hours = open_hours
        self._phone = phone

    def __str__(self) -> str:
        return f'Ksiegarnia: {self._street} {self._zip_code} ' \
               f'{self._city}, godziny {self._open_hours}, nr {self._phone}'


class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date: str,
                 birth_date: str, city: str, street: str,
                 zip_code: str, phone: str):
        self._first_name = first_name
        self._last_name = last_name
        self._hire_date = hire_date
        self._birth_date = birth_date
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._phone = phone

    def __str__(self) -> str:
        return f'Pracownik: {self._first_name} {self._last_name}, ' \
               f'zatrudniony {self._hire_date},  ' \
               f'urodzony {self._birth_date}, ' \
               f'nr {self._phone}, ' \
               f'adres {self._street} {self._zip_code} {self._city}'


class Book:
    def __init__(self, library: Library, publication_date: str,
                 author_name: str, author_surname: str,
                 number_of_pages: int):
        self._library = library
        self._publication_date = publication_date
        self._author_name = author_name
        self._author_surname = author_surname
        self._number_of_pages = number_of_pages

    def __str__(self) -> str:
        return f'Ksiazka: {self._publication_date}, {self._author_name} ' \
               f'{self._author_surname}, {self._number_of_pages} ' \
               f'stron, z {self._library}'


class Order:
    def __init__(self, employee: Employee, student: Student,
                 books: list, order_date: str):
        self._employee = employee
        self._student = student
        self._books = books
        self._order_date = order_date

    def __str__(self) -> str:
        return f'Zamowienie: \n ' \
               f'{self._employee}, \n ' \
               f'{self._student}, \n' \
               f' Ksiazki: \n ' + \
               ', \n '.join(str(book) for book in self._books) + ', \n' \
               f' Data zamowienia: {self._order_date}'
