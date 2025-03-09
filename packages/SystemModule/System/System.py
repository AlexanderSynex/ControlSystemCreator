from ..Connection import ConnectionManager

from .SystemRegressionModel import SystemRegressionModel

class System(object):
    def __init__(self, name : str = "", Inputs = [], Outputs = []):
        self.__name : str = name
        self.__Inputs = []
        self.__Outputs = []
        self.__weight = 0
        
        self.__model = SystemRegressionModel()
        self.add_inputs(Inputs)
        self.add_outputs(Outputs)
        
    
    @property
    def name(self):
        return self.__name
    
    @property
    def input_keys(self):
        return self.__Inputs
    
    @property
    def output_keys(self):
        return self.__Outputs
    
    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, weight):
        self.__weight = max(self.__weight, weight)
    
    @property
    def model_wrapper(self):
        return self.__model
    
    @property
    def model(self):
        return self.__model.model
    
    def add_input(self, name):
        ConnectionManager().get_instance(name)
        self.__Inputs.append(name)
        
        self.weight = ConnectionManager().get_instance(name).weight
        self.__model.inputs = len(self.__Inputs)
    
    
    def add_inputs(self, Inputs):
        for name in Inputs:
            self.add_input(name)
    
        
    def add_output(self, name):
        ConnectionManager().get_instance(name)
        self.__Outputs.append(name)
        ConnectionManager().get_instance(name).weight = self.__weight + 1
        self.__model.outputs = len(self.__Outputs)
    
        
    def add_outputs(self, Outputs):
        for name in Outputs:
            self.add_output(name)
    
        
    def print(self):
        print(f"system: {self.name}")
        print(f"weight={self.weight}")
        print(f"Inputs:")
        for i, link in enumerate(self.__Inputs):
            print(f"{i + 1}:\t{link} weight={ConnectionManager().get_instance(link).weight}")
        print(f"Outputs:")
        for i, link in enumerate(self.__Outputs):
            print(f"{i + 1}:\t{link} weight={ConnectionManager().get_instance(link).weight}")
        print(f"{self.__model.model=}")
        
    def fit(self, epochs=100):
        self.model_wrapper.fit(input_keys  = self.__Inputs, 
                               output_keys = self.__Outputs,
                               epochs=epochs)