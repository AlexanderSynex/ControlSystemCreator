from  packages.SystemModule.Singleton import Singleton

class DrawnItemsManager(metaclass=Singleton):
    __systems = {}
    __signals = {}

    def clear(cls):
        cls.__systems = {}
        cls.__signals = {}

    def __add(cls, item, collection : dict):
        collection[item.name] = item

    def __get(cls, name : str, collection : dict):
        if name not in collection:
            return None
        return collection[name]

    def __exists(cls, name : str, collection : dict):
        return name in collection
    
    def add_system(cls, item):
        cls.__add(item, cls.__systems)
        print(f"Systems drawn: {cls.__systems.keys()}")

    def add_signal(cls, item):
        cls.__add(item, cls.__signals)

    def get_system(cls, name):
        return cls.__get(name, cls.__systems)

    def get_signal(cls, name):
        return cls.__get(name, cls.__signals)

    def system_exists(cls, name):
        return cls.__exists(name, cls.__systems)

    def signal_exists(cls, name):
        return cls.__exists(name, cls.__signals)

    @property
    def systems(cls):
        return [name for name in cls.__systems]

    @property
    def signals(cls):
        return [name for name in cls.__signals]