# Metaclass
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# Manager purposed to store names of created systems and grant their uniqueness
class SystemNamesManager(metaclass=Singleton):
    names = []

    def add(cls, name):
        if name not in cls.names:
            cls.names.append(name)
    
    def clear(cls):
        cls.names = []
    
    def exists(cls, name):
        return name in cls.names
