from flask import Flask,jsonify
from flask_cors import CORS

def create_app():
    '''create and configure instance of our Flask application.'''
    app = Flask(__name__)
    CORS(app)
    #app.config['CORS_HEADERS']='Content-Type'

    @app.route('/')
    def root():
        return 'hello'

    return app
