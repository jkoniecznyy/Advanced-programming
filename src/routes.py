from flask import Flask, jsonify, request
from src.readMovies import movies

app = Flask(__name__)


@app.route('/api/moviese', methods=['GET'])
def getMovies():
    """

    """

    response = movies
    return jsonify(response), 200