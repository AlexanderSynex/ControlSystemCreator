import tensorflow as tf
import keras
from keras import layers

import numpy as np
from sklearn.model_selection import train_test_split

from packages.Utils import DBStorage

class SystemRegressionModel():
    def __init__(self, inputs : int = 1, outputs : int = 1):
        super().__init__()
        if inputs < 0: inputs = 1
        if outputs < 0: outputs = 1
        self.__model = keras.Sequential([])
        self.__optimizer = keras.optimizers.Adam()
        self.__loss = keras.losses.MeanSquaredLogarithmicError
        self.__metrics = [ keras.metrics.RootMeanSquaredError() ]
        self.__inputs = inputs
        self.__outputs = outputs
        self.__layers = [ ]
        self.__accuracy = 0
        self.__rebuild()


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
        self.__layers = [ max(self.__inputs, self.outputs) * 2 for _ in range(max(self.__inputs, self.__outputs)) ]
        layers_ = [layers.Input(shape=(self.__inputs,), name='Input'), 
                   layers.Dense(self.__inputs, activation=keras.activations.relu)]
        for i, layer in enumerate(self.__layers):
            layers_.append(layers.Dense(layer, activation=keras.activations.relu))
        layers_.append(layers.Dropout(0.2))
        layers_.append(layers.Dense(self.__outputs, activation=keras.activations.relu, name='Output'))
        self.__model = keras.Sequential(layers=layers_)
        
    def compile(self):
        self.model.compile(optimizer=self.__optimizer,
                           loss=self.__loss,
                           metrics=self.__metrics)
    
    @property
    def mse(self):
        return self.__accuracy
    
    def fit(self, input_keys : list, output_keys : list, epochs=500):
        inputs, outputs = [], []
        for signal in input_keys:
            x = DBStorage.find(signal)
            if not x.empty:
                inputs.append(x.to_list())
        for signal in output_keys:
            y = DBStorage.find(signal)
            if not y.empty:
                outputs.append(y.to_list())
        X = np.array(inputs).transpose()
        y = np.array(outputs).transpose()
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
        self.model.fit(X_train, y_train, epochs=epochs)
        self.__accuracy = self.model.evaluate(X_test, y_test)[1]
        
        print(self.model.summary())