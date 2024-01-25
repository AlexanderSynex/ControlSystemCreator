from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from packages.SystemModule import SystemManager, ConnectionManager

class QSystemDrawElement(QGraphicsItem):
    __width, __height = 100, 50
    __font_size = 10
    def __init__(self, name='', parent=None):
        super().__init__(parent=parent)
        
        self.__name = QStaticText()
        self.__name.setText(name)
        
        if not SystemManager().exists(name):
            return
        
        sys = SystemManager().get_instance(name)
        
        self.__ins = {}     #In Points
        self.__outs = {}    #Out Points
        
        for key in sys.input_keys:
            self.__ins[key] = QPointF(0, 0)
            
        for key in sys.output_keys:
            self.__outs[key] = QPointF(0, 0)
            
    
    def __update_text(self):
        rect = self.__nameItem.boundingRect()
        rect.moveBottomLeft(self.boundingRect().topLeft())
        
        self.__nameItem.setPos(rect.topLeft())
        
    

    def boundingRect(self):
        return QRectF(self.x(), self.y(),
                      self.__width, self.__height)
    
    
    def paint(self, painter, option, widget):
        # Drawing system rectangle
        painter.drawRect(self.boundingRect())
        
        # Drawing system name over system rect
        text_point = self.boundingRect().topLeft()
        text_point.setY(text_point.y() - QFontMetricsF(painter.font()).ascent() - painter.pen().widthF())
        painter.drawStaticText(text_point, QStaticText(self.__name))
        
        # Calculating ports' positions
        y_step = self.__height / (len(self.__ins) + 1)
        for i, port in enumerate(self.__ins):
            self.__ins[port].setX(self.boundingRect().x())
            self.__ins[port].setY(self.boundingRect().top() + y_step * (i + 1))
            
        
        y_step = self.__height / (len(self.__outs) + 1)
        for i, port in enumerate(self.__outs):
            self.__outs[port].setX(self.boundingRect().right())
            self.__outs[port].setY(self.boundingRect().top() + y_step * (i + 1))
        
        
        # Drawing connection points
        r = 3
        painter.setBrush(QBrush(Qt.GlobalColor.green))
        for port in self.__ins:
            painter.drawEllipse(self.__ins[port], r, r)

        painter.setBrush(QBrush(Qt.GlobalColor.red))
        for port in self.__outs:
            painter.drawEllipse(self.__outs[port], r, r)