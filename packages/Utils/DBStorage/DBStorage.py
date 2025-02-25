import pandas as pd

from packages.SystemModule.Singleton import Singleton

class DBStorage(metaclass=Singleton):
    __db : pd.DataFrame = pd.DataFrame([])
    
    @classmethod
    def load(cls, path : str) -> bool:
        cls.__db = pd.read_csv(path)
        cls.__fill_missing()
        return True
    
    @classmethod
    def __fill_missing(cls):
        pass

    @classmethod
    def empty(cls) -> bool:
        return cls.__db.empty
    
    @classmethod
    def data(cls) -> pd.DataFrame:
        return cls.__db
    
    @classmethod
    def titles(cls) -> list:
        return list(cls.__db.columns.values)
    
    @classmethod
    def find(cls, name) -> pd.Series | None:
        if cls.empty():
            return None
        if name not in cls.titles():
            return None
        return cls.__db[name]