from .System import System
from ..Singleton import Singleton

# Manager purposed to store names of created systems and grant their uniqueness
class SystemManager(metaclass=Singleton):
    _systems = {}

    def __add(cls, system):
        name = system.name
        if name not in cls._systems:
            print(f"SystemManager. System created: {name}")
            cls._systems[name] = system
    
    def __get(cls, name):
        if name not in cls._systems:
            return None
        return cls._systems[name]
    
    def get_instance(cls, name : str = "", Inputs = [], Outputs = []):
        system = cls.__get(name)
        if system is None:
            system = System(name, Inputs=Inputs, Outputs=Outputs)
            cls.__add(system)
        return system
    
    def clear(cls):
        cls.names = {}
    
    def exists(cls, name):
        return cls.__get(name) != None
    
    def empty(cls):
        return not cls._systems
    
    # Return all keys
    def get_keys(cls):
        return list(cls._systems.keys())