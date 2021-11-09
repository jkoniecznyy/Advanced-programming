# Task 1
class Student:
    def __init__(self, name: str, mark: int):
        self._name = name
        self._mark = mark

    def is_passed(self) -> bool:
        return self._mark > 50

    def __str__(self) -> str:
        return f'Student: {self._name}'
