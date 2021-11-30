import csv

from src.classes.Movie import Movie
from src.classes.Link import Link
from src.classes.Raiting import Rating
from src.classes.Tag import Tag


def read_movies_from_csv() -> list[Movie]:
    with open('src/csv_files/movies.csv', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        movies = []
        for row in csv_reader:
            movies.append(Movie(row[0], row[1],
                                row[2].split("|")))
        return movies[1:]


def read_links_from_csv() -> list[Link]:
    with open('src/csv_files/links.csv', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        links = []
        for row in csv_reader:
            links.append(Link(row[0], row[1],
                                row[2]))
        return links[1:]


def read_ratings_from_csv() -> list[Rating]:
    with open('src/csv_files/ratings.csv', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        raitings = []
        for row in csv_reader:
            raitings.append(Rating(row[0], row[1],
                                row[2], row[3]))
        return raitings[1:]


def read_tags_from_csv() -> list[Tag]:
    with open('src/csv_files/tags.csv', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        tags = []
        for row in csv_reader:
            tags.append(Tag(row[0], row[1],
                                row[2], row[3]))
        return tags[1:]
