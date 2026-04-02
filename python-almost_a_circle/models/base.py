#!/usr/bin/python3
"""Base class for all other classes in this project"""
import json


class Base:
    """Base class to manage id attribute across all classes"""
    
    __nb_objects = 0
    
    def __init__(self, id=None):
        """Initialize Base instance with id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        list_dicts = []
        if list_objs is not None:
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(list_dicts))
    
    @staticmethod
    def from_json_string(json_string):
        """Return list of JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy
    
    @classmethod
    def load_from_file(cls):
        """Return a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                list_dicts = cls.from_json_string(file.read())
            return [cls.create(**dict_obj) for dict_obj in list_dicts]
        except FileNotFoundError:
            return []
