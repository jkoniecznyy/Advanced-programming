if __name__ == '__main__':
    from flask import Flask
    from flask_restful import Api, Resource
    from src.read_movies import read_movies_from_csv

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

    api.add_resource(Movies, '/api/movies')

    app.run(host='0.0.0.0', port=5000, debug=True)
