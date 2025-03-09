import numpy as np

from packages.SystemModule.Singleton import Singleton

from packages.SystemModule.System import SystemManager
from packages.SystemModule.Connection import ConnectionManager

class SystemNeuralModeling(metaclass=Singleton):
    @classmethod
    def feed_forward_system(cls,system_name):
        if not SystemManager().exists(system_name):
            return
        system = SystemManager().get_instance(system_name)
            
        # Making input for current system
        x = np.zeros(len(system.input_keys))
        for i, input in enumerate(system.input_keys):
            if ConnectionManager().exists(input):
                x[i] = ConnectionManager().get_instance(input).value
        x = np.array([[xi] for xi in x]).reshape((1, -1))
        y = system.model.predict(x)
        
        for i, output in enumerate(system.output_keys):
            if ConnectionManager().exists(output):
                ConnectionManager().get_instance(output).value = y[0, i]
                print(f"{system_name}.{output}={ConnectionManager().get_instance(output).value}")
    
    @classmethod
    def feed_forward_from_signal(cls,signal_name):
        print(f"Here: {signal_name}")
        if not ConnectionManager().exists(signal_name):
            return
        
        systems = list(ConnectionManager().get_instance(signal_name).to_systems)
        
        for system_name in systems:
            if not SystemManager().exists(system_name):
                continue
            system = SystemManager().get_instance(system_name)
            SystemNeuralModeling.feed_forward_system(system_name)
            
            # # Making input for current system
            # x = np.zeros(len(system.input_keys))
            # for i, input in enumerate(system.input_keys):
            #     if ConnectionManager().exists(input):
            #         x[i] = ConnectionManager().get_instance(input).value
            # x = np.array([[xi] for xi in x]).reshape((1, -1))
            # y = system.model.predict(x)
            
            # for output in system.output_keys:
            #     if not ConnectionManager().exists():
            #         continue
                    