from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class QDataController(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.__init_UI()
    

    def __init_UI(self):
        self.__layout = QVBoxLayout()
        self.__load_button = QPushButton('Load')

        self.__layout.addWidget(self.__load_button,0)
        self.__layout.addWidget(QFrame(), 1)

        self.setLayout(self.__layout)
