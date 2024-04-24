class Car:
    def __init__(self, car_number_id, brand, country, model, parking_id):
        self.car_number_id = car_number_id
        self.brand = brand
        self.country = country
        self.model = model
        self.parking_id = parking_id

class Parking:
    def __init__(self, parking_number_id, location):
        self.parking_number_id = parking_number_id
        self.location = location