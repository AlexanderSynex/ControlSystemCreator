from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class QConnectionPort(QGraphicsItem):
    def __init__(self, link_name, parent = None):
        super().__init__(parent)
        
        self.__name = link_name
        self.__radius = 2
    
    
    
    @property
    def name(self):
        return self.__name
    
    @property
    def center(self):
        return self.mapToParent(self.boundingRect().center())
    
    def boundingRect(self):
        r = self.__radius
        return QRectF(-r/2, -r/2,
                      r, r)
    
    def paint(self, painter, option, widget):
        r = self.__radius
        # print(f"Draw {self.__name} port at {self.boundingRect().center()}")
        painter.drawText(self.boundingRect().topLeft(), self.name)
        painter.drawEllipse(self.boundingRect().center(), r, r)