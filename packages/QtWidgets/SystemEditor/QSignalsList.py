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
        
    def checked_inputs(self) -> list:
        signals=[]
        for row_i in range(self.count()):
            item : QLinkItem = self.itemWidget(self.item(row_i))
            if item.input:
                signals.append(item.text())
        return signals
    
    def checked_outputs(self) -> list:
        signals=[]
        for row_i in range(self.count()):
            item : QLinkItem = self.itemWidget(self.item(row_i))
            if item.output:
                signals.append(item.text())
        return signals
    
    def uncheck(self):
        for row_i in range(self.count()):
            self.itemWidget(self.item(row_i)).clear()
    
    
    def display_checked(self, inputs=None, outputs=None):
        if inputs:
            for signal in inputs:
                for row_i in range(self.count()):
                    item : QLinkItem = self.itemWidget(self.item(row_i))
                    if item.text() is signal:
                        item.input = True
        if outputs:
            for signal in outputs:
                for row_i in range(self.count()):
                    item : QLinkItem = self.itemWidget(self.item(row_i))
                    if item.text() is signal:
                        item.output = True