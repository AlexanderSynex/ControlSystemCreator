from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from packages.SystemModule import SystemManager, ConnectionManager

class QSystemDrawElement(QGraphicsItem):
    __width, __height = 100, 50
    __font_size = 10
    def __init__(self, name='', parent=None):
        super().__init__(parent=parent)
        
        self.__name = QStaticText(name)
        self.__ins = {}     #In Points
        self.__outs = {}    #Out Points
        
        if not SystemManager().exists(name):
            return
        
        sys = SystemManager().get_instance(name)
        
        for key in sys.input_keys:
            self.__ins[key] = QPointF(0, 0)
            
        for key in sys.output_keys:
            self.__outs[key] = QPointF(0, 0)
            
        self.__update_ports()
    

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
        self.__update_ports()
        
        # Drawing connection points
        r = 2
        painter.setBrush(QBrush(Qt.GlobalColor.green))
        for (port, point) in self.__ins.items():
            painter.drawEllipse(point, r, r)

        painter.setBrush(QBrush(Qt.GlobalColor.red))
        for (port, point) in self.__outs.items():
            painter.drawEllipse(point, r, r)
            
    
    def __update_ports(self):
        y_step = self.__height / (len(self.__ins) + 1)
        for i, (port_name, point) in enumerate(self.__ins.items()):
            point.setX(self.x())
            point.setY(self.y() + y_step * (i + 1))
            self.__ins[port_name] = point
        
        y_step = self.__height / (len(self.__outs) + 1)
        for i, (port_name, point) in enumerate(self.__outs.items()):
            point.setX(self.boundingRect().right())
            point.setY(self.y() + y_step * (i + 1))
            self.__outs[port_name] = point
            
    @property
    def input_points(self):
        return [self.boundingRect().topLeft() + self.mapToScene(p) for (_, p) in self.__ins.items()]
    
    @property
    def output_points(self):
        return [self.boundingRect().topLeft() + self.mapToScene(p) for (_, p) in self.__outs.items()]