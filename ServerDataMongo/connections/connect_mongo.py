import os

from dotenv import load_dotenv
from pymongo import MongoClient


class ConnectMongo:
    def __init__(self):
        self.load_env()

    def load_env(self):
        env_path = os.path.join(os.path.dirname(__file__), '..', '..', 'app.env')
        load_dotenv(env_path)

    def connect(self):
        host = os.getenv('PYTHON_DATASOURCE_MONGO_HOST')
        port = os.getenv('PYTHON_DATASOURCE_MONGO_PORT')
        db_name = os.getenv('PYTHON_DATASOURCE_MONGO_DB')
        mongo_uri = f'mongodb://{host}:{port}/'
        client = MongoClient(mongo_uri)
        return client[db_name]