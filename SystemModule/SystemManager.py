from .ISystem import ISystem
from .Singleton import Singleton

# Manager purposed to store names of created systems and grant their uniqueness
class SystemManager(metaclass=Singleton):
    systems = {}

    def __add(cls, system):
        name = system.get_name()
        if name not in cls.systems:
            print(name)
            cls.systems[name] = system
    
    def __get(cls, name):
        if name in cls.systems:
            return cls.systems[name]
        return None
    
    def get_instance(cls, name : str = "", Inputs = [], Outputs = []):
        system = cls.__get(name)
        if system is None:
            system = ISystem(name, Inputs=Inputs, Outputs=Outputs)
            cls.__add(system)
        return system
    
    def clear(cls):
        cls.names = {}
    
    def exists(cls, name):
        return name in cls.systems
