class ISystem:
    def __init__(self, name : str = "", Inputs = [], Outputs = []):
        self.name : str = name
        self.Inputs = Inputs
        self.Outputs = Outputs
        
    def get_name(self):
        return self.name