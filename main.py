from flask import Flask
from flask_restful import Api, Resource

from src.read_functions.read_functions import read_from_csv

app = Flask(__name__)
api = Api(app)


@app.route('/api/status', methods=['GET'])
def getNetworkStatus():
    """
        :rtype: str
    """
    return 'The network is working properly'


class Movies(Resource):

    def get(self):
        return [movie.__dict__ for movie in read_from_csv("Movie")]


class Links(Resource):

    def get(self):
        return [link.__dict__ for link in read_from_csv("Link")]


class Ratings(Resource):

    def get(self):
        return [rating.__dict__ for rating in read_from_csv("Rating")]


class Tags(Resource):

    def get(self):
        return [tag.__dict__ for tag in read_from_csv("Tag")]


api.add_resource(Movies, '/api/movies')
api.add_resource(Links, '/api/links')
api.add_resource(Ratings, '/api/ratings')
api.add_resource(Tags, '/api/tags')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
