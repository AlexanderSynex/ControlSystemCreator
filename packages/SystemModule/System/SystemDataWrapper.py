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
        
        inputs = []
        for name in SystemManager().get_instance(system_name).input_keys:
            inputs.append(ConnectionDataWrapper().to_dict(link_name=name))
        
        outputs = []
        for name in SystemManager().get_instance(system_name).output_keys:
            outputs.append(ConnectionDataWrapper().to_dict(link_name=name))
        
        return dict(name=system_name, inputs=inputs, outputs=outputs)
    
    
    def from_dict(cls, system_dict : dict):
        if not all(key in system_dict for key in ('name',
                                                  'weight',
                                                  'inputs', 
                                                  'outputs')):
            return
        
        input_keys = ConnectionDataWrapper().from_dicts(system_dict['inputs'])
        output_keys = ConnectionDataWrapper().from_dicts(system_dict['outputs'])
        
        SystemManager().get_instance(name=system_dict['name'],
                                     Inputs=input_keys,
                                     Outputs=output_keys)
        
        ConnectionManager().rebase_internal_connections()
    
    
    def to_json(cls, system_name : str) -> str:
        if not SystemManager().exists(system_name):
            return None
        
        return json.dumps(cls.to_dict(system_name=system_name), indent=2)
    
    
    def from_json(cls, path : str):
        with open(path) as file:
            raw_data = json.load(file)
            
            if 'systems' not in raw_data:
                return
            
            for system in raw_data['systems']:
                cls.from_dict(system)
    
    
    def all_to_dict(cls):
        if SystemManager().empty():
            return dict(systems=[])
        
        systems=[]
        for name in SystemManager().get_keys():
            systems.append(cls.to_dict(name))
        
        return dict(systems=systems)
    
    
    def all_to_json(cls) -> str:
        if SystemManager().empty():
            return json.dumps(systems=[])
        
        return json.dumps(cls.all_to_dict(), indent=2)
    
    
    