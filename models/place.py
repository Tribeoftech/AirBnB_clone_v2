#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
from models import storage
import os


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', ForeignKey('places.id'),
                             nullable=False, primary_key=True),
                      Column('amenity_id', ForeignKey('amenities.id'),
                             nullable=False, primary_key=True))


class Place(BaseModel, Base):
    """Defining Place class"""
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review',
                               cascade='all, delete, delete-orphan',
                               backref='place')
        amenities = relationship('Amenity', secondary='place_amenity',
                                 viewonly=False, backref='place_amenities')

    else:
        @property
        def reviews(self):
            """Getter for reviews"""
            reviewList = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    reviewList.append(review)
            return reviewList

        @property
        def amenities(self):
            """Getter for amenities"""
            amenList = []
            for amenity in storage.all(Amenity).values():
                if self.id == amenity.place_id:
                    amenList.append(amenity)
            return amenList

        @amenities.setter
        def amenities(self, obj):
            """Setter for amenities"""
            if isinstance(obj, Amenity):
                self.append(obj)
