#! /usr/bin/env python3
from uuid import uuid4
from datetime import datetime
from models import storage


"""
Defines base objects that has common characteristics
for its sub_class
"""


class BaseModel:
    """
    Represent a model that shows
       defines uniqueness of each instance.
        Instance Variables:
        id: uuid object that gives a unique id to an instance
        created_at : a datetime object that assigns the current date
        the object was created
        update_at : a datetime object  that assigns the current when
        the object is created and updated
        __str__ : a string representation of the model
        Methods:
            save : update the update_at variable
            to_dict : returns dictionary representation of the model
    """
    def __init__(self):
        """
        For initialization of instance variables
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """
         updates the update_at variable with current date
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        my_dict = self.__dict__.copy()
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        my_dict["__class__"] = str(self.__class__.__name__)
        return my_dict

    def __str__(self):
        """returns string representation"""
        return "[{}] ({}) {}". \
            format(type(self).__name__, self.id, self.__dict__)

    def __init__(self, *args, **kwargs):
        """
        Create a BasmodelModel object from a named argument
        :param args: None
        :param kwargs: named argument to initialize the object argument
        """
        if kwargs and kwargs != {}:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        storage.new(self)
