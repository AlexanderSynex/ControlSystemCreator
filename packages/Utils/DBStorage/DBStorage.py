import pandas as pd

from packages.SystemModule.Singleton import Singleton

class DBStorage(metaclass=Singleton):
    __db : pd.DataFrame = pd.DataFrame([])

    def load(cls, path : str):
        cls.__db = pd.read_csv(path)
        cls.__fill_missing()
    

    def __fill_missing(cls):
        pass



    def empty(cls) -> bool:
        return cls.__db.empty
    

    def data(cls) -> pd.DataFrame:
        return cls.__db