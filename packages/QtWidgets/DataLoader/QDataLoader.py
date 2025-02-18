from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from .QDataLoaderControl import QDataLoaderControl

class QDataLoader(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.__init_UI()
    

    def __init_UI(self):
        self.__layout = QHBoxLayout()

        self.__table = QTableWidget()
        self.__control = QDataLoaderControl()

        self.__layout.addWidget(self.__table)
        self.__layout.addWidget(self.__control,0)
        
        self.setLayout(self.__layout)
        
        
    