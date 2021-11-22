if __name__ == '__main__':
    from flask import Flask
    from flask_restful import Api
    from src.Movie import Movies

    app = Flask(__name__)
    api = Api(app)

    @app.route('/api/status', methods=['GET'])
    def getNetworkStatus():
        """
            :rtype: str
        """
        return 'The network is working properly'

    api.add_resource(Movies, '/api/movies')

    app.run(host='0.0.0.0', port=5000, debug=True)
