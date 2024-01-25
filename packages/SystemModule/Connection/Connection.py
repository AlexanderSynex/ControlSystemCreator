class Connection(object):
    def __init__(self, name : str, value :float = 0):
        self.__name = name
        self.__value = value
        
        self.__weight = 0
        self.__connectors = set()
    
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
    
    
    def add_connector(self, name):
        self.__connectors.add(name)
        
        
    def print(self):
        print(f"Link. {self.__name}={self.__value}. Connected with: {self.__connectors}")