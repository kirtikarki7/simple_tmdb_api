import logging

from flask import Flask
from flask_restful import Api

from tmdb_app.resource import BasicTmdb
import settings

logging.basicConfig(format='[%(asctime)s][%(levelname)-2s][%(name)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
                            level=logging.INFO)
app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = settings.app_secret_key

api.add_resource(BasicTmdb, '/<string:resource>/<int:resource_id>', 
                        '/<string:resource>/<int:resource_id>/<string:specific>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
