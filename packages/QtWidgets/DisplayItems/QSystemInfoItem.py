from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class QSystemInfo(QWidget):
    def __init__(self, system, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.system = system
        
        self.__init_UI()
        
        
    def __init_UI(self):
        self.__layout = QVBoxLayout(self)
        
        self.__name_label = QLabel()
        self.__input_label = QLabel()
        self.__output_label = QLabel()
        
        self.__layout.addWidget(self.__name_label)
        self.__layout.addWidget(self.__input_label)
        self.__layout.addWidget(self.__output_label)
        
        self.update_system_info()
    
    
    def update_system_info(self):
        
        self.__name_label.setText(f"<b>Name</b>={self.system.get_name()}")
        self.__input_label.setText(f"<b>Inputs</b>: {len(self.system.get_input_keys())}")
        self.__output_label.setText(f"<b>Outputs</b>: {len(self.system.get_output_keys())}")