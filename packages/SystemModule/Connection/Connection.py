class Connection(object):
    def __init__(self, name : str, value :float = 0):
        self.__name = name
        self.__value = value
        
        self.__weight = 0
    
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
        print("Connection. Weight setter")
        return self.__weight
    
    @weight.setter
    def weight(self, value):
        print("Connection. Weight getter")
        self.__weight = max(self.__weight, value)
    

