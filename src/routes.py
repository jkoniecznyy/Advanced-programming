from flask import Flask, jsonify, request
from src.readMovies import movies
from src.Movie import MovieEncoder

app = Flask(__name__)


@app.route('/api/networkstatus', methods=['GET'])
def getNetworkStatus():
    """
        :rtype: str
    """
    return 'The network is working properly'


@app.route('/api/movies', methods=['GET'])
def getMovies():
    """

    """
    moviesJSON = {}
    for movie in movies:
        moviesJSON[movie.id] = (MovieEncoder().encode(movie))
        print(movie.id)
        print(movie)
        print(MovieEncoder().encode(movie))
    print(moviesJSON)
    return moviesJSON, 200
