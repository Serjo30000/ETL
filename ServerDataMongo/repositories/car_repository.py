from ServerDataMongo.connections.connect_mongo import ConnectMongo
from ServerDataMongo.models.models import Car


class CarRepository:
    def __init__(self):
        connect_mongo = ConnectMongo()
        self.db = connect_mongo.connect()

    def create(self, data):
        car = Car(car_number_id=data.car_number_id, brand=data.brand, country=data.country, model=data.model, parking_id=data.parking_id)
        car_collection = self.db['cars']
        car_collection.insert_one(car.__dict__)

    def read_all(self):
        car_collection = self.db['cars']
        return car_collection.find()