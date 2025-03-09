from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class QNamedValueBox(QWidget):

    def __init__(self, property, min = 0, max = 100, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.__property = property
        
        self.__init_UI(min, max)
        
        
    def __init_UI(self, min, max):
        self.__layout = QHBoxLayout(self)
        
        self.__name_label = QLabel(self.__property)
        self.__value_edit = QSpinBox()
        self.__value_edit.setRange(min, max)
        
        self.__layout.addWidget(self.__name_label, 2)
        self.__layout.addWidget(self.__value_edit, 4)
        
    @property
    def value(self): return self.__value_edit.value()