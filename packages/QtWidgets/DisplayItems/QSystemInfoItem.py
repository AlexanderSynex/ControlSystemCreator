from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class QSystemInfo(QWidget):
    def __init__(self, system, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.system = system
        
        self.__layout = QVBoxLayout(self)
        self.__layout.addWidget(QLabel(f"<b>Name</b>={self.system.get_name()}"))
        self.__layout.addWidget(QLabel(f"<b>Inputs</b>: {0}"))
        self.__layout.addWidget(QLabel(f"<b>Outputs</b>: {0}"))