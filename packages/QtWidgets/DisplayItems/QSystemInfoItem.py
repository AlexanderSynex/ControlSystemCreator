from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from ...SystemModule import SystemManager


class QSystemInfo(QWidget):
    def __init__(self, system_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.system_name = system_name
        
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
        
        if not SystemManager().exists(self.system_name):
            return
        
        system = SystemManager().get_instance(self.system_name)
        
        self.__name_label.setText(f"<b>Name</b>: {system.get_name()}")
        self.__input_label.setText(f"<b>Inputs</b>: {len(system.get_input_keys())}")
        self.__output_label.setText(f"<b>Outputs</b>: {len(system.get_output_keys())}")