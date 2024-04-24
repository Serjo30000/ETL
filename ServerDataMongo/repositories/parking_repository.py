from ServerDataMongo.connections.connect_mongo import ConnectMongo
from ServerDataMongo.models.models import Parking


class ParkingRepository:
    def __init__(self):
        connect_mongo = ConnectMongo()
        self.db = connect_mongo.connect()

    def create(self, data):
        parking = Parking(parking_number_id=data.parking_number_id, location=data.location)
        parking_collection = self.db['parkings']
        parking_collection.insert_one(parking.__dict__)

    def read_all(self):
        car_collection = self.db['parkings']
        return car_collection.find()