import numpy as np

from packages.SystemModule.Singleton import Singleton

from packages.SystemModule.System import SystemManager
from packages.SystemModule.Connection import Connection, ConnectionManager

from collections import deque

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
        print(f"System={system_name}")
        for i, output in enumerate(system.output_keys):
            if ConnectionManager().exists(output):
                ConnectionManager().get_instance(output).value = y[0, i]
                print(f"\t{output}={ConnectionManager().get_instance(output).value}")
    
    
    @classmethod
    def feed_forward_from_signal(cls,signal_name):
        print(f"Here: {signal_name}")
        if not ConnectionManager().exists(signal_name):
            return
        visited = set()
        
        systems : set = ConnectionManager().get_instance(signal_name).to_systems
        next_systems = set()
        for system_name in systems:
            if not SystemManager().exists(system_name):
                continue
            system = SystemManager().get_instance(system_name)
            visited.add(system_name)
            SystemNeuralModeling.feed_forward_system(system_name)
            for output in system.output_keys:
                if not ConnectionManager().exists(output):
                        continue
                signal = ConnectionManager().get_instance(output)
                next_systems = next_systems.union(signal.to_systems)
        for system in next_systems:
            SystemNeuralModeling.feed_forward_system(system)
    
    @classmethod
    def system_next_systems(cls, system_name) -> set:
        if not SystemManager().exists(system_name):
            return set()
        
        system = SystemManager().get_instance(system_name)
        systems = set()
        for signal_name in system.output_keys:
            if not ConnectionManager().exists(signal_name):
                continue
            signal = ConnectionManager().get_instance(signal_name)
            systems = systems.union(signal.to_systems)
        return systems
    
    @classmethod
    def recalculate(cls):
        # find input signals
        inputs = set()
        for signal_name in ConnectionManager().get_keys():
            signal : Connection = ConnectionManager().get_instance(signal_name)
            if not signal.from_system and signal.to_systems:
                inputs.add(signal_name)
        
        # set of systems
        systems = deque()
        for signal_name in inputs:
            signal : Connection = ConnectionManager().get_instance(signal_name)
            for system_name in signal.to_systems:
                if (SystemManager().exists(system_name)):
                    systems.append(system_name)
        
        while systems:
            system_name = systems.popleft()
            cls.feed_forward_system(system_name=system_name)
            # feed forward
            neighbours = cls.system_next_systems(system_name=system_name)
            for system in neighbours:
                systems.append(system)
        
        # get output signals
        # find set of systems from outputs <- exit condition