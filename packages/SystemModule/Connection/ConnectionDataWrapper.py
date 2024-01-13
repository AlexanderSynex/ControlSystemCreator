from ..Singleton import Singleton
from .Connection import Connection
from .ConnectionManager import ConnectionManager

import pandas as pd

import json

class ConnectionDataWrapper(metaclass=Singleton):
    def load_from_csv(cls, path):
        print(f"ConnectionDWrapper. Loading links from <{path}>")
        names = pd.read_csv(path).columns.values
        
        new_names = []
        for name in names:
            if not ConnectionManager().exists(name):
                new_names.append(name)
            ConnectionManager().get_instance(name)
            
        return new_names
    
    
    def to_dict(cls, link_name : str) -> dict:
        if not ConnectionManager().exists(link_name):
            return None
        
        link = ConnectionManager().get_instance(name=link_name)
        
        return dict(name=link_name, 
                    value=link.value,
                    weight=link.weight)
    
    
    def from_dict(cls, link_dict : dict):
        if not all(key in link_dict for key in ('name', 'value', 'weight')):
            return
        
        link = ConnectionManager().get_instance(name=link_dict['name'], 
                                                value=link_dict['value'])
        
        link.weight = link_dict['weight']
        
        return link_dict['name']
    
    
    def from_dicts(cls, link_dict_list : list):
        links = []
        for link_dict in link_dict_list:
            links.append(cls.from_dict(link_dict=link_dict))
        return links
    
    
    def to_json(cls, link_name : str) -> str:
        if not ConnectionManager().exists(link_name):
            return None
        
        return json.dumps(cls.to_dict(link_name))