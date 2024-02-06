from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from packages.SystemModule.Connection import ConnectionManager

from .Items import QConnectionItemWidget

class QConnectionList(QListWidget):
    
    value_changed = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        
    def add_signal(self, name):
        
        if not ConnectionManager().exists(name):
            return
        
        widget = QConnectionItemWidget(signal_name=name)
        item = QListWidgetItem(parent=self)
        item.setSizeHint(widget.minimumSizeHint())
        
        widget.value_changed.connect(self.value_changed)
        
        self.setItemWidget(item, widget)
        
    
    def add_signals(self, names):
        for name in names:
            self.add_signal(name=name)