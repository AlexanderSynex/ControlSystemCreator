from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from packages.SystemModule import SystemManager, ConnectionManager

from .QConnectionPort import QConnectionPort

class QSystemDrawElement(QGraphicsItem):
    __width, __height = 100, 50
    __font_size = 10
    def __init__(self, name='', parent=None):
        super().__init__(parent=parent)
        
        self.__name = name
        self.__in_ports = []     #In Points
        self.__out_ports = []    #Out Points
        
        self.__init_ports()
    
    
    def __init_ports(self):
        sys = SystemManager().get_instance(self.__name)

        y_step = self.__height / (len(sys.input_keys) + 1)
        for i, link_name in enumerate(sys.input_keys):
            port = QConnectionPort(link_name, parent=self)
            port.moveBy(0, y_step * (i + 1))
            self.__in_ports.append(port)
            
        y_step = self.__height / (len(sys.output_keys) + 1)
        for i, link_name in enumerate(sys.output_keys):
            port = QConnectionPort(link_name, parent=self)
            port.moveBy(self.boundingRect().width(), y_step * (i + 1))
            self.__out_ports.append(port)
        

    def boundingRect(self):
        return QRectF(0, 0,
                      self.__width, self.__height)
    
    
    def paint(self, painter, option, widget):
        # Drawing system rectangle
        print(self.boundingRect())
        painter.drawRect(self.boundingRect())
        # Drawing system name over system rect
        painter.drawText(self.boundingRect().topLeft(), self.__name)


    def input_port(self, name):
        for port in self.__in_ports:
            if port.name == name:
                return port
        return None


    def output_port(self, name):
        #return {n: self.boundingRect().topLeft() + self.mapToScene(p) for (n, p) in self.__outs.items()}
        for port in self.__out_ports:
            if port.name == name:
                return port
        return None

            
    @property
    def input_ports(self):
        # return {n: self.boundingRect().topLeft() + self.mapToScene(p) for (n, p) in self.__ins.items()}
        return self.__in_ports

    @property
    def output_ports(self):
        #return {n: self.boundingRect().topLeft() + self.mapToScene(p) for (n, p) in self.__outs.items()}
        return self.__out_ports

    @property
    def name(self):
        return self.__name