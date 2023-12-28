class ISystem:
    def __init__(self, name : str = "", Inputs = [], Outputs = []):
        self.name : str = name
        self.Inputs = Inputs
        self.Outputs = Outputs
        
    def get_name(self):
        return self.name
    
    def add_inputs(self, Inputs):
        self.Inputs.append(Inputs)
        
    def add_outputs(self, Outputs):
        self.Outputs.append(Outputs)