from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from packages.SystemModule import ConnectionManager

class QSignalDrawElement(QGraphicsItem):
    def __init__(self, p1 : QPointF, p2 : QPointF, parent=None):
        super().__init__(parent=parent)
        
        self.__name = ""
        self.__value = 0
        self.__line = QLineF(p1, p2)
        
    #    self.__update_value()
        
    
    # def __update_value(self):        
    #     if ConnectionManager().exists(self.__name):
    #         self.__value = ConnectionManager().get_instance(self.__name).value()
    
    
    @property
    def line(self):
        return self.p1(), self.p2()
    
    @line.setter
    def line(self, p1 : QPointF, p2 : QPointF):
        self.__line.setP1(p1)
        self.__line.setP2(p2)
        
    def boundingRect(self):                                         # TODO
        return QRectF(self.__line.p1(), self.__line.p2())
    
    
    def paint(self, painter, option, widget):                       # TODO
        painter.drawLine(self.__line)