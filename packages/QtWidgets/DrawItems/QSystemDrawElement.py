from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class QSystemDrawElement(QGraphicsRectItem):
    def __init__(self, name='', parent=None):
        super().__init__(0, 0, 100, 50, parent=parent)
        
        self.__name = name
        
        self.__input_ports = {}
        self.__output_ports = {}

        self.__nameItem = QGraphicsTextItem(self.__name, self)
        
        self.__update_text()
    
    def __update_text(self):
        rect = self.__nameItem.boundingRect()
        rect.moveBottomLeft(self.boundingRect().topLeft())
        
        self.__nameItem.setPos(rect.topLeft())
