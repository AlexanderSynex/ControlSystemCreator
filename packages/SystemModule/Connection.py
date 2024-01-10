class Connection:
    def __init__(self, name : str, value :float = 0):
        self.__name = name
        self.__value = value
    
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value : float):
        self.__value = value
    
    @property
    def name(self):
        return self.__name
