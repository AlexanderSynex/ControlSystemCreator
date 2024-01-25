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
            self.__ins[key] = 0
            
        for key in sys.output_keys:
            self.__outs[key] = 0
            
    
    def __update_text(self):
        rect = self.__nameItem.boundingRect()
        rect.moveBottomLeft(self.boundingRect().topLeft())
        
        self.__nameItem.setPos(rect.topLeft())
        
    

    def boundingRect(self):                                         # TODO
        return QRectF(self.x(), self.y(),
                      self.__width, self.__height)
    
    
    def paint(self, painter, option, widget):                       # TODO
        painter.drawRect(self.boundingRect())
        
        
        text_point = self.boundingRect().topLeft()
        text_point.setY(text_point.y() - QFontMetricsF(painter.font()).ascent() - painter.pen().widthF())
        
        painter.drawStaticText(text_point, QStaticText(self.__name))
        
        painter.setBrush(QBrush(Qt.GlobalColor.green))
        r = 3
        y_step = self.__height / (len(self.__ins) + 1)
        
        x, y = self.boundingRect().x(), self.boundingRect().top() + y_step
        for port in self.__ins:
            painter.drawEllipse(QPointF(x, y), r, r)
            y += y_step
        
        
        painter.setBrush(QBrush(Qt.GlobalColor.red))
        y_step = self.__height / (len(self.__outs) + 1)
        
        x, y = self.boundingRect().right(), self.boundingRect().top() + y_step
        for port in self.__outs:
            painter.drawEllipse(QPointF(x, y), r, r)
            y += y_step