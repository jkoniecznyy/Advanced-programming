from src.Movie import Movie
import csv


with open('src/movies.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    movies = []
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        elif line_count > 6:
            break
        else:
            line_count += 1
            movies.append(Movie(row[0], row[1], row[2].split("|")))
            # print(Movie(row[0], row[1], row[2].split("|")))