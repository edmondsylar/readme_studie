from flask import Flask
from views.routes import my_blueprint

api = Flask(__name__)
api.register_blueprint(my_blueprint, url_prefix='/api/v1')
