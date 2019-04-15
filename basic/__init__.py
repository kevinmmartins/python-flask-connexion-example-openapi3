import connexion
from flask_cors import CORS
from flask_marshmallow import Marshmallow

from basic.config.log_config import create_log

ma = Marshmallow()
logger = create_log()


def init_api():
    app = connexion.App(__name__, specification_dir="./openapi/")
    app.add_api("swagger.yaml", arguments={"title": "files"})
    CORS(app.app)
    ma.init_app(app.app)
    return app
