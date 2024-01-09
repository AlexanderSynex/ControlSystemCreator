from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from ..SystemModule import SystemManager

from .DisplayItems import QSystemInfo

class QSystemSelector(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        
    def add_system(self, system_name):
        
        if not SystemManager().exists(system_name):
            return
        
        sys = SystemManager().get_instance(system_name)
        
        widget = QSystemInfo(system=sys)
        item = QListWidgetItem(parent=self)
        item.setSizeHint(widget.minimumSizeHint())
        self.setItemWidget(item, widget)