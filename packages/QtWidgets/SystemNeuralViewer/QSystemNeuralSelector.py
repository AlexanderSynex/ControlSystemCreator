from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from packages import SystemManager

from .Items import QSystemNeuralInfo

class QSystemNeuralSelector(QListWidget):
    system_selected = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.itemActivated.connect(lambda item: self.system_selected.emit(self.itemWidget(item).name()))
        
    def add_system(self, system_name):
        
        if not SystemManager().exists(system_name):
            return
        
        widget = QSystemNeuralInfo(system_name=system_name)
        item = QListWidgetItem(parent=self)
        item.setSizeHint(widget.minimumSizeHint())
        self.setItemWidget(item, widget)
        
    
    def add_systems(self, system_names):
        for name in system_names:
            self.add_system(system_name=name)
            
    def update_data(self):
        for i in range(self.count()):
            item = self.item(i)
            widget : QSystemNeuralInfo = self.itemWidget(item)
            widget.update_system_info()