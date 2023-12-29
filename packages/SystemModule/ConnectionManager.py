from .Singleton import Singleton
from .Connection import Connection

import pandas as pd

class ConnectionManager(metaclass=Singleton):
    __links = {}
    __internal_link_number = 1
    
    def __add(cls, link):
        name = link.get_name()
        if name not in cls.__links:
            print(f"ConnectionManager. Link added: {name}")
            cls.__links[name] = link
    
    
    def __get(cls, name):
        if name in cls.__links:
            return cls.__links[name]
        return None
    
    
    def clear(cls):
        cls.__links = {}
        cls.__internal_link_number = 1
    
    
    def get_instance(cls, name : str, value : float = 0):
        link = cls.__get(name)
        if link is None:
            link = Connection(name, value)
            cls.__add(link)
        return link
    
    
    def get_instances(cls, names = []):
        # Return all keys
        if not names:
            return list(cls.__links.keys())
        
        links = []
        for name in names:
            link = cls.__get(name)
            if link is not None:
                links.append(link)
            
        return links
    
    
    #Add specific number of internal links
    def create_internal_connection(cls, link_number : int = 1):
        links = []
        for i in range(link_number):
            name = f"_link{cls.__internal_link_number}"
            links.append(cls.get_instance(name))
            cls.__internal_link_number += 1
        
        return links
    
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