#!/usr/bin/python3
""" Class place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ Class place """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    amenity_ids = []
    latitude = 0.0
    longitude = 0.0
