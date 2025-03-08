from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from .Items import *

class QSignalList(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        
        
    def add(self
                , parameter : str
                , input : bool = False
                , output : bool = False):
        item = QListWidgetItem()
        widget = QLinkItem(name=parameter)
        item.setSizeHint(widget.minimumSizeHint())
        self.addItem(item)
        self.setItemWidget(item, widget)