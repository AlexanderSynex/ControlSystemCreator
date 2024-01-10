from ..Singleton import Singleton
from .System import System
from .SystemManager import SystemManager

from ..Connection import ConnectionDataWrapper

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