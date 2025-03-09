from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from packages.SystemModule.Connection import (ConnectionManager)

from packages.SystemModule.System import (SystemManager)

from packages.QtWidgets.SystemEditor import QSystemSelector
from .QNeuralModelViewer import QNeuralModelViewer

class QSystemNeuralViewer(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.__init_UI()
    
    
    def __init_UI(self):
        self.__layout = QHBoxLayout()
        
        self.__model_viewer = QNeuralModelViewer()
        self.__system_selector = QSystemSelector()
        self.__fit_button = QPushButton('Fit models')
        
        
        
        control_layout = QVBoxLayout()
        control_layout.addWidget(self.__system_selector, 1)
        control_layout.addWidget(self.__fit_button, 0)
        
        self.__layout.addWidget(self.__model_viewer, 4)
        self.__layout.addLayout(control_layout, 1)
        self.setLayout(self.__layout)
        
        self.__system_selector.system_selected.connect(self.__model_viewer.show)
        self.__fit_button.clicked.connect(self.fit_systems)
        
        
    def update_systems(self):
        print(f"Update systems. {SystemManager().get_keys()}")
        self.__system_selector.add_systems(SystemManager().get_keys())
        
    
    def fit_systems(self):
        for system_name in SystemManager().get_keys():
            print(f"Compiling {system_name=}")
            system = SystemManager().get_instance(system_name)
            system.model_wrapper.compile()
            system.fit()