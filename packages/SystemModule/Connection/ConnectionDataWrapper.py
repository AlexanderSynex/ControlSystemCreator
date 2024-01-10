from ..Singleton import Singleton
from .Connection import Connection
from .ConnectionManager import ConnectionManager

import pandas as pd

import json

class ConnectionDataWrapper(metaclass=Singleton):
    def load_from_csv(cls, path):
        print(f"ConnectionDWrapper. Loading links from <{path}>")
        names = pd.read_csv(path).columns.values
        
        for name in names:
            ConnectionManager().get_instance(name)
    
    
    def to_dict(cls, link_name : str) -> dict:
        if not ConnectionManager().exists(link_name):
            return None
        
        link = ConnectionManager().get_instance(name=link_name)
        
        return dict(name=link_name, 
                    value=link.value)
    
    
    def to_json(cls, link_name : str) -> str:
        if not ConnectionManager().exists(link_name):
            return None
        
        return json.dumps(cls.to_dict(link_name))