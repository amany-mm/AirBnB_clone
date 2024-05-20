#!/usr/bin/python3
""" Class Review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Class Review """
    user_id = ""
    place_id = ""
    text = ""
