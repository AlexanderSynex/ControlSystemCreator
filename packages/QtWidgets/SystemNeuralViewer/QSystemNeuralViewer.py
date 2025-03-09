from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from packages.SystemModule.Connection import (ConnectionManager)

from packages.SystemModule.System import (SystemManager)

from packages.QtWidgets.SystemEditor import QSystemSelector

class QSystemNeuralViewer(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.__init_UI()
    
    
    def __init_UI(self):
        self.__layout = QHBoxLayout()
        
        self.__model_viewer = QFrame()
        self.__system_selector = QSystemSelector()
        
        self.__layout.addWidget(self.__model_viewer, 4)
        self.__layout.addWidget(self.__system_selector, 1)
        self.setLayout(self.__layout)
        
        
    def update_systems(self):
        print(f"Update systems. {SystemManager().get_keys()}")
        self.__system_selector.add_systems(SystemManager().get_keys())