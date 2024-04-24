from flask import Flask, jsonify

from ServerDataPostgres.models.models import Car, Parking
from ServerDataPostgres.repositories.car_repository import CarRepository
from ServerDataPostgres.repositories.parking_repository import ParkingRepository

app = Flask(__name__)

parking_repository = ParkingRepository()
car_repository = CarRepository()


def run_script():
    print("Start postgres")
    new_parking = Parking(location='Parking A')
    parking_repository.create(new_parking)
    parkings = parking_repository.read_all()
    print("Parking add in postgres")
    new_car = Car(brand='Toyota', country='Japan', model='Camry', parking_id=parkings[-1].id)
    car_repository.create(new_car)
    print("Car add in postgres")

@app.route('/cars')
def getAllCars():
    cars = car_repository.read_all()
    cars_dict = [car.to_dict() for car in cars]
    return jsonify(cars_dict)

@app.route('/parkings')
def getAllParking():
    parkings = parking_repository.read_all()
    parkings_dict = [parking.to_dict() for parking in parkings]
    return jsonify(parkings_dict)

if __name__ == '__main__':
    print("Hello world!")
    run_script()
    app.run(debug=True, host='app_postgres', port=5000)

