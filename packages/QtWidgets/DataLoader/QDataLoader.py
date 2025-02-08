from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class QDataLoader(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.__init_UI()
    

    def __init_UI(self):
        self.__layout = QHBoxLayout()

        self.__table = QTableWidget()

        self.__layout.addWidget(self.__table)
        self.setLayout(self.__layout)
        
        
    