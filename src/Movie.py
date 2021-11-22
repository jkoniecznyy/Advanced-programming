import csv
from dataclasses import dataclass
from flask_restful import Resource


@dataclass
class Movie:

    id: int
    title: str
    genres: str


class Movies(Resource):

    def __init__(self):
        with open('src/movies.csv', encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            self._movies = []
            for row in csv_reader:
                if line_count != 0:
                    self._movies.append(Movie(row[0], row[1],
                                              row[2].split("|")))
                else:
                    line_count += 1

    def get(self):
        return [movie.__dict__ for movie in self._movies]
