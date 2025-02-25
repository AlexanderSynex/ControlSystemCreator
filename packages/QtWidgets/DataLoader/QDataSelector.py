from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from packages.Utils.DBStorage import DBStorage

from .Items import QDataItem

class QDataSelector(QListWidget):
    
    plot_changed = pyqtSignal(str, bool)
    
    def __init__(self, parent = None):    
        super().__init__(parent)
        self.itemChanged.connect(self.display_item)
    
    def display_item(self, item : QListWidgetItem):
        self.plot_changed.emit(item.text(), item.checkState() is Qt.CheckState.Checked)
    
    def display(self, titles : list):
        self.clear()
        for title in titles:
            self.addItem(QDataItem(title))
        