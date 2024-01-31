class Connection(object):
    def __init__(self, name : str, value :float = 0):
        self.__name = name
        self.__value = value
        
        self.__weight = 0
        self.__from_systems = ""
        self.__to_systems = set()
    
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value : float):
        self.__value = value
    
    @property
    def name(self):
        return self.__name

    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, value):
        self.__weight = max(self.__weight, value)
    
    
    @property
    def from_systems(self):
        return self.__from_systems
    
    @property
    def to_systems(self):
        return self.__to_systems
    
    def add_from_system(self, name):
        self.__from_systems = name
        
        
    def add_to_system(self, name):
        self.__to_systems.add(name)
        
        
    def print(self):
        print(f"Link: {self.__name}\n",
              f"\tValue={self.__value}\n",
              f"\tFrom: {self.__from_systems}\n",
              f"\tTo: {self.__to_systems}")