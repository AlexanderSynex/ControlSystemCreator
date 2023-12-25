from .Singleton import Singleton
from .Connection import Connection

class ConnectionManager(metaclass=Singleton):
    _links = {}
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
    
    def get_instance(cls, name : str, value : float = 0):
        link = cls.__get(name)
        if link is None:
            link = Connection(name, value)
            cls.__add(link)
        return link
    
    def exists(cls, name):
        return cls.__get(name) != None
