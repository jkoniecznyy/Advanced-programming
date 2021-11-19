from typing import Iterable
from json import JSONEncoder


class Movie:
    def __init__(self, mid: int, title: str, genres: list):
        self._id = mid
        self._title = title
        self._genres = genres

    def __str__(self) -> str:
        return f'Id: {self._id}, title: {self._title} ' \
               f'genres: {self._genres}'

    def __dir__(self) -> Iterable[str]:
        return super().__dir__()

    @property
    def id(self):
        return self._id


class MovieEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
