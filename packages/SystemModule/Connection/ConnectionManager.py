from ..Singleton import Singleton
from .Connection import Connection

import re

class ConnectionManager(metaclass=Singleton):
    __links = {}
    __internal_link_number = 1
    
    def __add(cls, link):
        name = link.name
        if name not in cls.__links:
            print(f"ConnectionManager. Link added: {name}")
            cls.__links[name] = link
    
    
    def __get(cls, name):
        if name in cls.__links:
            return cls.__links[name]
        return None
    
    
    def clear(cls):
        print(f"ConnectionManager. Links deleted")
        cls.__links = {}
        cls.__internal_link_number = 1
    
    
    def __set_internal_number(self, n):
        __internal_link_number = max(__internal_link_number, n)
    
    
    def get_instance(cls, name : str, value : float = 0):
        link = cls.__get(name)
        if link is None:
            link = Connection(name, value)
            cls.__add(link)
        return link
    
    
    def get_instances(cls, names = []):
        links = []
        for name in names:
            links.append(cls.get_instance(name))
        return links
    
    
    # Return all keys
    def get_keys(cls):
        return list(cls.__links.keys())
    
    
    #Add specific number of internal links
    def create_internal_connections(cls, link_number : int = 1):
        links = []
        for i in range(link_number):
            name = f"_link{cls.__internal_link_number}"
            links.append(name)
            cls.__internal_link_number += 1
        
        return links
    
    
    def rebase_internal_coonections(cls):
        for key in cls.get_keys():
            if '_link' in key:
                possible_values = [int(val) for val in re.findall('\d+', key)]
                n = max(possible_values)
                cls.__internal_link_number = n + 1
    
    
    def set_value(cls, name : str, value : float):
        link = cls.__get(name)
        if link is not None:
            link.value = value
    
    
    def exists(cls, name):
        return cls.__get(name) != None