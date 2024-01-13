from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from ...SystemModule import ConnectionManager


class QConnectionItemWidget(QWidget):
    def __init__(self, signal_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.signal_name = signal_name
        
        self.__init_UI()
        
        
    def __init_UI(self):
        self.__layout = QVBoxLayout(self)
        
        self.__name_label = QLabel()
        self.__value_edit = QDoubleSpinBox()
        
        self.__layout.addWidget(self.__name_label)
        self.__layout.addWidget(self.__value_edit)
        
        self.update_system_info()
    
    
    def update_system_info(self):
        
        if not ConnectionManager().exists(self.signal_name):
            return
        
        link = ConnectionManager().get_instance(self.signal_name)
        
        self.__name_label.setText(f"<b>Name</b>: {link.name}")
        self.__value_edit.setValue(link.value)
        
        
        