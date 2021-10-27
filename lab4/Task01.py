# Task 1
class Student:
    def __init__(self, name: str, mark: int):
        self.name = name
        self.mark = mark

    def is_passed(self) -> bool:
        return self.mark > 50

    def __str__(self) -> str:
        return f'Student: {self.name}'
