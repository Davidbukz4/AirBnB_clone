#!/usr/bin/python3
'''
File Storage
'''
import os
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place
        'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review
        }


class FileStorage:
    '''
    Serializes instances to a JSON file
    and deserializes JSON file to instances
    '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        ''' Returns the dictionary __objects '''
        return self.__objects

    def new(self, obj):
        ''' sets in __objects the obj with key <obj class name>.id '''
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        value = obj
        dic = {key: value}
        self.__objects.update(dic)

    def save(self):
        ''' serializes __objects to the JSON file (path: __file_path) '''
        with open(self.__file_path, 'w') as f:
            objs = {}
            for key, value in self.__objects.items():
                objs[key] = value.to_dict()
            json.dump(objs, f)

    def reload(self):
        '''
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        '''
        try:
            if os.path.exists(self.__file_path):
                with open(self.__file_path) as f:
                    objs = json.load(f)
                for key, value in objs.items():
                    obj_class = key.split('.')[0]
                    self.__objects[key] = classes[obj_class](**value)
        except Exception:
            pass
