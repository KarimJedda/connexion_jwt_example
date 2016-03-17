import connexion
import logging
import pathlib
from authentication import authenticate, identity
from flask_jwt import JWT, jwt_required, current_identity
import os

connexion.api.SWAGGER_UI_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'swagger-ui-mod')

def start_stuff():
	logging.basicConfig(level=logging.ERROR)
	app = connexion.App(__name__)
	app.add_api(pathlib.Path('api.yaml'))
	application = app.app
	application.config['SECRET_KEY'] = 'super-secret'
	jwt = JWT(application, authenticate, identity)

	app.run(server='gevent', port=9878)