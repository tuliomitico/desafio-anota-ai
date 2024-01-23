import typing as t

from flask import Flask

from .config.mongo.mongo_db_config import MongoDBConfig

def setup_app(app: Flask) -> None:
    MongoDBConfig().mongo_configure().init_app(app=app)

def create_app(config = None) -> Flask:
    app = Flask(__name__)
    return app