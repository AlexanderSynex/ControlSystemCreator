class ISystem:
    def __init__(self, name : str = "", Inputs = [], Outputs = []):
        self.__name : str = name
        self.__Inputs = Inputs
        self.__Outputs = Outputs
    
    @property
    def name(self):
        return self.__name
    
    @property
    def input_keys(self):
        links = []
        for link in self.__Inputs:
            links.append(link.name)
        return links
    
    @property
    def output_keys(self):
        links = []
        for link in self.__Outputs:
            links.append(link.name)
        return links
    
    def add_inputs(self, Inputs):
        self.__Inputs.append(Inputs)
        
    def add_outputs(self, Outputs):
        self.__Outputs.append(Outputs)
        
    def print(self):
        print(f"system: {self.get_name()}")
        print(f"Inputs:")
        print(self.__Inputs)
        for i, link in enumerate(self.__Inputs):
            print(f"{i + 1}:\t{link.get_name()}")
        print(f"Outputs:")
        for i, link in enumerate(self.__Outputs):
            print(f"{i + 1}:\t{link.get_name()}")