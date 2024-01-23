from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class QSystemDrawElement(QGraphicsItem):
    __width, __height = 100, 50
    __font_size = 10
    def __init__(self, name='', parent=None):
        super().__init__(parent=parent)
        
        self.__name = QStaticText()
        self.__name.setText(name)
        
        self.__ins = {'in_1' : 0, 'in_2' : 0}     #In Points
        self.__outs = {'out_1':1}    #Out Points
    
    
    def __update_text(self):
        rect = self.__nameItem.boundingRect()
        rect.moveBottomLeft(self.boundingRect().topLeft())
        
        self.__nameItem.setPos(rect.topLeft())
        
    

    def boundingRect(self):                                         # TODO
        return QRectF(self.x(), self.y(),
                      self.__width, self.__height)
    
    
    def paint(self, painter, option, widget):                       # TODO
        painter.drawRect(0, 0, self.__width, self.__height)
        
        
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