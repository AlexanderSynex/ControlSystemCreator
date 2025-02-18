from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

import pandas as pd
import numpy as np 

from packages.Utils.DBStorage import DBStorage

class PandasTableModel(QAbstractTableModel):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return self._data.columns.values[section]
            return 'Column {}'.format(section + 1)
        return super().headerData(section, orientation, role)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if index.isValid():
            if role == Qt.ItemDataRole.DisplayRole:
                return QVariant(str(
                    self._data.iloc[index.row()].iloc[index.column()]))
        return QVariant()


class QDataViewer(QTableView):
    
    def __init__(self): 
        super().__init__()


    def redraw_table(self):
        if DBStorage().empty():
            return
        
        df = DBStorage().data()
        self.setModel(PandasTableModel(df))