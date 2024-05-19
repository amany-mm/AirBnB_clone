#!/usr/bin/python3
""" BaseModel that defines all common attributes and
methods for other classes. """
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ BaseModel of models """

    def __init__(self, *args, **kwargs):
        """ new object instantiation """

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) > 0:

            for k, v in kwargs.items():
                if k == "created_at":
                    self.created_at = datetime.strptime(v,
                                                        '%Y-%m-%dT%H:%M:%S.%f')

                elif k == "updated_at":
                    self.updated_at = datetime.strptime(v,
                                                        '%Y-%m-%dT%H:%M:%S.%f')

                else:
                    if k != "__class__":
                        setattr(self, k, v)

        else:
            models.storage.new(self)

    def __str__(self):
        """ Returns string object representation. """

        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__)

    def save(self):
        """ Updates attr updated_at with current time. """

        self.updated_at = datetime.now()

        models.storage.save()

    def to_dict(self):
        """ Returns key and values instance __dict__. """

        _dict = self.__dict__.copy()

        _dict["__class__"] = self.__class__.__name__

        _dict["created_at"] = self.created_at.isoformat()
        _dict["updated_at"] = self.updated_at.isoformat()
        return _dict
