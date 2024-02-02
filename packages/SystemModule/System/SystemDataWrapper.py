from ..Singleton import Singleton
from .System import System
from .SystemManager import SystemManager

from ..Connection import ConnectionManager, ConnectionDataWrapper

import pandas as pd

import json

class SystemDataWrapper(metaclass=Singleton):
    def to_dict(cls, system_name : str) -> dict:
        if not SystemManager().exists(system_name):
            return {}
        
        sys = SystemManager().get_instance(system_name)
        
        inputs = [name for name in sys.input_keys]        
        outputs = [name for name in sys.output_keys]
        
        return dict(name=system_name, inputs=inputs, outputs=outputs)

    
    def to_json(cls, system_name : str) -> str:
        if not SystemManager().exists(system_name):
            return None
        
        return json.dumps(cls.to_dict(system_name=system_name), indent=2)

    
    def all_to_dict(cls):
        if SystemManager().empty():
            return dict(signals=[],systems=[])
        
        signals=[]
        for name in ConnectionManager().get_keys():
            signals.append(ConnectionDataWrapper().to_dict(link_name=name))
        
        systems=[]
        for name in SystemManager().get_keys():
            systems.append(cls.to_dict(name))
        
        return dict(signals=signals, systems=systems)
    
    
    def all_to_json(cls) -> str:
        return json.dumps(cls.all_to_dict(), indent=2)
    
    
    def from_dict(cls, system_dict : dict):
        if not all(key in system_dict for key in ('name',
                                                  'inputs', 
                                                  'outputs')):
            return
        
        input_keys = system_dict['inputs']
        output_keys = system_dict['outputs']
        
        SystemManager().get_instance(name=system_dict['name'],
                                     Inputs=input_keys,
                                     Outputs=output_keys)
        
        ConnectionManager().rebase_internal_connections()
    
    
    def from_json(cls, path : str):
        with open(path) as file:
            raw_data = json.load(file)
            
            if not all(key in raw_data for key in ('systems', 'signals')):
                return
            
            for signal in raw_data['signals']:
                ConnectionDataWrapper().from_dict(signal)
            
            for system in raw_data['systems']:
                cls.from_dict(system)