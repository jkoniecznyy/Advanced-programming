import csv

from src.classes.Movie import Movie
from src.classes.Link import Link
from src.classes.Raiting import Rating
from src.classes.Tag import Tag


def read_from_csv(type: str) -> list:
    match type:
        case "Movie":
            with open('src/csv_files/movies.csv', encoding="utf8") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                result = []
                for row in csv_reader:
                    result.append(Movie(row[0], row[1],
                                        row[2].split("|")))
        case "Link":
            with open('src/csv_files/links.csv', encoding="utf8") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                result = []
                for row in csv_reader:
                    result.append(Link(row[0], row[1],
                                   row[2]))

        case "Rating":
            with open('src/csv_files/ratings.csv', encoding="utf8") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                result = []
                for row in csv_reader:
                    result.append(Rating(row[0], row[1],
                                     row[2], row[3]))
        case "Tag":
            with open('src/csv_files/tags.csv', encoding="utf8") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                result = []
                for row in csv_reader:
                    result.append(Tag(row[0], row[1],
                                  row[2], row[3]))
    return result[1:]