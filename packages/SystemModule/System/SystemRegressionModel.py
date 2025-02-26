import tensorflow as tf
import keras
from keras import layers


class SystemRegressionModel():
    def __init__(self, inputs : int = 1, outputs : int = 1):
        super().__init__()
        if inputs < 0: inputs = 1
        if outputs < 0: outputs = 1
        self.__model = keras.Sequential([])
        self.__inputs = inputs
        self.__outputs = outputs
        self.__hidden = [ max(self.__inputs, self.__outputs) * 2,
                          max(self.__inputs, self.__outputs) * 3,
                          max(self.__inputs, self.__outputs) * 2  ]
    
    @property
    def inputs(self) -> int: return self.__inputs
    
    @inputs.setter
    def inputs(self, value : int): 
        if value > 0: 
            self.__inputs = value
        self.__rebuild()
    
    @property
    def outputs(self) -> int: return self.__outputs
    
    @outputs.setter
    def outputs(self, value : int): 
        if value > 0: 
            self.__outputs = value
        self.__rebuild()
    
    @property
    def model(self) -> keras.Sequential: return self.__model
    
    def __rebuild(self):
        layers_ = [layers.Dense(self.__inputs)]
        for layer in self.__hidden:
            layers_.append(layers.Dense(layer))
        layers_.append(layers.Dense(self.__outputs))
        self.__model = keras.Sequential(layers=layers_)