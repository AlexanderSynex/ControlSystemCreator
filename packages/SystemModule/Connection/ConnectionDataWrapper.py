from ..Singleton import Singleton
from .Connection import Connection
from .ConnectionManager import ConnectionManager

import pandas as pd

class ConnectionDataWrapper(metaclass=Singleton):
    def load_from_csv(cls, path):
        print(f"ConnectionDWrapper. Loading links from <{path}>")
        names = pd.read_csv(path).columns.values
        
        for name in names:
            ConnectionManager().get_instance(name)