from ServerDataMongo.models.models import Car, Parking
from ServerDataMongo.repositories.car_repository import CarRepository
from ServerDataMongo.repositories.parking_repository import ParkingRepository
import requests

class DbSyncService:
    def __init__(self):
        self.car_repository = CarRepository()
        self.parking_repository = ParkingRepository()
        self.base_url = 'http://app_postgres:5000'

    def carSyncOnDb(self):
        response = requests.get(self.base_url + '/cars')
        if response.status_code == 200:
            api_cars = response.json()
        else:
            print('Ошибка при получении данных:', response.status_code)
            return

        old_cars = self.car_repository.read_all()

        existing_car_ids = [car['car_number_id'] for car in old_cars]

        for api_car in api_cars:
            if api_car['id'] not in existing_car_ids:
                car = Car(
                    car_number_id=api_car['id'],
                    brand=api_car['brand'],
                    country=api_car['country'],
                    model=api_car['model'],
                    parking_id=api_car['parking_id']
                )
                self.car_repository.create(car)

        new_cars = self.car_repository.read_all()

        for new_car in new_cars:
            print(new_car)

    def parkingSyncOnDb(self):
        response = requests.get(self.base_url + '/parkings')
        if response.status_code == 200:
            parkings = response.json()
        else:
            print('Ошибка при получении данных:', response.status_code)
            return

        old_parkings = self.parking_repository.read_all()

        existing_parking_ids = [parking['parking_number_id'] for parking in old_parkings]

        for api_parking in parkings:
            if api_parking['id'] not in existing_parking_ids:
                parking = Parking(
                    parking_number_id=api_parking['id'],
                    location=api_parking['location']
                )
                self.parking_repository.create(parking)

        new_parkings = self.parking_repository.read_all()

        for new_parking in new_parkings:
            print(new_parking)