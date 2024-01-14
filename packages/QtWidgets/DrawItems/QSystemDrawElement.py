from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class QSystemDrawElement(QGraphicsRectItem):
    def __init__(self, name='', parent=None):
        super().__init__(0, 0, 50, 50, parent=parent)
        
        self.__input_ports = {} # Coordinates
        self.__output_ports = {} # Coordinates

        self.nameItem = QGraphicsSimpleTextItem(name, self)
