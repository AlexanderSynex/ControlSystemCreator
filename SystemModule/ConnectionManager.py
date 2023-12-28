from .Singleton import Singleton
from .Connection import Connection

import pandas as pd

class ConnectionManager(metaclass=Singleton):
    _links = {}
    __internal_link_number = 1
    
    def __add(cls, link):
        name = link.get_name()
        if name not in cls._links:
            print(f"Link added: {name}")
            cls._links[name] = link
    
    
    def __get(cls, name):
        if name in cls._links:
            return cls._links[name]
        return None
    
    
    def clear(cls):
        cls._links = {}
        cls.__internal_link_number = 1
    
    
    def get_instance(cls, name : str, value : float = 0):
        link = cls.__get(name)
        if link is None:
            link = Connection(name, value)
            cls.__add(link)
        return link
    
    
    def get_instances(cls):
        return list(cls._links.keys())
    
    
    #Add specific number of internal links
    def create_internal_connection(cls, link_number : int = 1):
        for i in range(link_number):
            name = f"_link{cls.__internal_link_number}"
            cls.get_instance(name)
            cls.__internal_link_number += 1
    
    def set_value(cls, name : str, value : float):
        link = cls.__get(name)
        if link is not None:
            link.set_value(value)
    
    
    def exists(cls, name):
        return cls.__get(name) != None
    
    
    def load_from_csv(cls, path):
        cls.clear()    
        names = pd.read_csv(path).columns.values
        
        for name in names:
            cls.get_instance(name)