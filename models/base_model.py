""" Base model module to defines all common attributes
and methods for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """ defines all common attributes and methods for other classes """
    def __init__(self) -> None:
        """ public instance attributes """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ object string format """
        return ("[{}] ({}) {}")\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ update updated_at with the current datetime. """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ instance attributes set will be returned, class name and
        iso format dates. """
        _dict = self.__dict__.copy()
        _dict["__class__"] = self.__class__.__name__
        _dict["created_at"] = _dict["created_at"].isoformat()
        _dict["updated_at"] = _dict["updated_at"].isoformat()
        return _dict
