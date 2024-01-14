from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class QSystemDrawElement(QGraphicsRectItem):
    __width, __height = 100, 50
    def __init__(self, name='', parent=None):
        super().__init__(0, 0, __width, __height, parent=parent)
        
        self.__name = name
        
        self.__input_ports = {}
        self.__output_ports = {}

        self.__nameItem = QGraphicsTextItem(self.__name, self)
        
        self.__update_text()
    
    
    def __update_text(self):
        rect = self.__nameItem.boundingRect()
        rect.moveBottomLeft(self.boundingRect().topLeft())
        
        self.__nameItem.setPos(rect.topLeft())
        
    @property
    def collision(self):
        text_rect = self.__nameItem.boundingRect()
        return __width + text_rect.width(), __height + text_rect.height()