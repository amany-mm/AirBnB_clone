#!/usr/bin/python3
""" Class User module"""
from models.base_model import BaseModel


class User(BaseModel):
    """ Class User """

    first_name = ""
    last_name = ""
    email = ""
    password = ""
