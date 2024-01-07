class ISystem:
    def __init__(self, name : str = "", Inputs = [], Outputs = []):
        self.__name : str = name
        self.__Inputs = Inputs
        self.__Outputs = Outputs
        
    def get_name(self):
        return self.__name
    
    def add_inputs(self, Inputs):
        self.__Inputs.append(Inputs)
        
    def add_outputs(self, Outputs):
        self.__Outputs.append(Outputs)
        
    def print(self):
        print(f"system: {self.get_name()}")
        print(f"Inputs:")
        for i, link in enumerate(self.__Inputs):
            print(f"{i + 1}:\t{link.get_name()}")
        print(f"Outputs:")
        for i, link in enumerate(self.__Outputs):
            print(f"{i + 1}:\t{link.get_name()}")