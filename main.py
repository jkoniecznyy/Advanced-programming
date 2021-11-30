if __name__ == '__main__':
    from flask import Flask
    from flask_restful import Api, Resource
    from src.read_functions.read_functions import read_movies_from_csv,\
        read_links_from_csv, read_tags_from_csv, read_ratings_from_csv

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
            return [movie.__dict__ for movie in read_movies_from_csv()]

    class Links(Resource):

        def get(self):
            return [link.__dict__ for link in read_links_from_csv()]

    class Ratings(Resource):

        def get(self):
            return [rating.__dict__ for rating in read_ratings_from_csv()]

    class Tags(Resource):

        def get(self):
            return [tag.__dict__ for tag in read_tags_from_csv()]

    api.add_resource(Movies, '/api/movies')
    api.add_resource(Links, '/api/links')
    api.add_resource(Ratings, '/api/ratings')
    api.add_resource(Tags, '/api/tags')

    app.run(host='0.0.0.0', port=5000, debug=True)
