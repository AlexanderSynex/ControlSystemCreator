class Connection:
    def __init__(self, name : str, value :float = 0):
        self.name : str = name
        self.value : float = value
    
    def get_value(self):
        return self.value
            
    def get_name(self):
        return self.name