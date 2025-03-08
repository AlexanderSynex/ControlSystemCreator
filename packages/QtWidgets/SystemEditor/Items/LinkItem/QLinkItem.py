from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from .QIOCheckGroup import QIOCheckGroup

class QLinkItem(QWidget):
    
    def __init__(self, name : str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__name = name
        self.__init_UI()
        
    def __init_UI(self):
        self.__layout = QHBoxLayout(self)
        self.__name_label = QLabel(text=self.__name)
        self.__io_checker = QIOCheckGroup()
        self.__layout.addWidget(self.__name_label, stretch=1)
        self.__layout.addWidget(self.__io_checker, stretch=0, alignment=Qt.AlignmentFlag.AlignRight)
    
    def text(self) -> str:
        return self.__name
    
    @property
    def input(self) -> bool:
        return self.__io_checker.input
    
    @input.setter
    def input(self, checked : bool):
        self.__io_checker.input = checked
    
    @property
    def output(self) -> bool:
        return self.__io_checker.output
    
    @output.setter
    def output(self, checked : bool):
        self.__io_checker.output = checked
    
    def clear(self):
        self.__io_checker.clear()