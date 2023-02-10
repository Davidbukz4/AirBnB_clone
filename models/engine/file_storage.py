#!/usr/bin/python3
"""
FileStorage
"""
import json
import os


class FileStorage:
    """Serializes instances to a JSON file and \
        deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects.update({key: obj})

    def save(self):
        """serializes __objects to the JSON file"""
        dict_fmt = FileStorage.__objects.copy()
        dict_fmt = {k: v.to_dict() for k, v in dict_fmt.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(dict_fmt, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            if os.path.exists(FileStorage.__file_path):
                with open(FileStorage.__file_path, 'r') as f:
                    json_object = json.load(f)
                for key, value in json_object.items():
                    FileStorage.__objects[key] = value
        except FileNotFoundError:
            pass
