#!/usr/bin/python3
'''
BASE MODEL
'''


from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    ''' Defines common attributes/methods for other classes '''
    def __init__(self, *args, **kwargs):
        ''' public initializes instances '''
        if kwargs:
            del kwargs['__class__']
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        ''' Returns a string representation of the object '''
        return '[{}] ({}) {}'.format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        ''' updates the attribute "updated_at" with the current time '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        ''' returns a dictionary containing all keys/values of the instance'''
        dic_objs = self.__dict__.copy()
        dic_objs['__class__'] = self.__class__.__name__
        dic_objs['created_at'] = dic_objs['created_at'].isoformat()
        dic_objs['updated_at'] = dic_objs['updated_at'].isoformat()
        return dic_objs
