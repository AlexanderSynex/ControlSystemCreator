from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from packages.SystemModule.Connection import ConnectionManager


class QConnectionItemWidget(QWidget):
    def __init__(self, signal_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.signal_name = signal_name
        
        self.__init_UI()
        
        
    def __init_UI(self):
        self.__layout = QHBoxLayout(self)
        
        self.__name_label = QLabel()        
        self.__value_edit = QDoubleSpinBox()
        
        self.__value_edit.setReadOnly(True)
        
        self.__layout.addWidget(self.__name_label, 2)
        self.__layout.addWidget(self.__value_edit, 4)

        
        self.update_system_info()
    
    
    def update_system_info(self):
        
        if not ConnectionManager().exists(self.signal_name):
            return
        
        link = ConnectionManager().get_instance(self.signal_name)
        
        self.__name_label.setText(f"{link.name}")
        self.__value_edit.setValue(link.value)
        
        
        