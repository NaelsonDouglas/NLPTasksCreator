import flask
from flask import request, jsonify
import logging
from flask_cors import CORS

class PublicApi():
        def __init__(self):
                self.app = flask.Flask(__name__)
                CORS(self.app)
                self.app.config["DEBUG"] = True

        def start(self):
                @self.app.route('/get', methods=['GET'])
                def api_id():
                        return {'a':1}

                self.app.run(host='0.0.0.0', port=2020)
