from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    brand = Column(String)
    country = Column(String)
    model = Column(String)
    parking_id = Column(Integer, ForeignKey('parkings.id'))

    def to_dict(self):
        return {
            'id': self.id,
            'brand': self.brand,
            'country': self.country,
            'model': self.model,
            'parking_id': self.parking_id
        }

class Parking(Base):
    __tablename__ = 'parkings'

    id = Column(Integer, primary_key=True)
    location = Column(String)
    cars = relationship('Car')

    def to_dict(self):
        return {
            'id': self.id,
            'location': self.location
        }