import csv

from src.Movie import Movie as Movie


def read_movies_from_csv() -> list[Movie]:
    with open('src/movies.csv', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        movies = []
        for row in csv_reader:
            movies.append(Movie(row[0], row[1],
                                row[2].split("|")))
        return movies[1:]
