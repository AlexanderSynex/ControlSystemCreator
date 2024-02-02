from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from packages.SystemModule import ConnectionManager

from .DrawnItemsManager import DrawnItemsManager


# Элемент для отрисовки данных между портами систем
# Отображает название и значение сигнала
class QSignalDrawElement(QGraphicsItem):
    def __init__(self, name = "", parent=None):
        super().__init__(parent=parent)
        
        self._name = name
        self._value = 0
        
        self._from_point = QPointF()
        self._to_points = []

        self._from_point, self._to_point = self._parse_link_to_points()

        print(f"Signal={self.name} From=({self.from_point.x()}, {self.from_point.y()}), To={self.to_points}")
    
    
    def update_value(self):
        if (ConnectionManager().exists(self._name)):
            self._value = ConnectionManager().get_instance(self._name).value

    @property
    def from_point(self):
        return self._from_point
    
    @property
    def to_points(self):
        return self._to_point

    @property
    def name(self):
        return self._name
    

    def boundingRect(self):
        min_x, max_x = self.from_point.x(), self.from_point.x()
        min_y, max_y = self.from_point.y(), self.from_point.y()
        
        for p in self.to_points:
            if p.x() < min_x: min_x = p.x()
            if p.x() > max_x: min_x = p.x()
            if p.y() < min_y: min_y = p.x()
            if p.y() > max_y: max_y = p.x()
        
        return QRectF(QPointF(min_x, min_y), QPointF(max_x, max_y))
    

    def paint(self, painter, option, widget):
        self._from_point, self._to_point = self._parse_link_to_points()
        for to_point in self.to_points:
            painter.drawLine(self.from_point, to_point)
        
        self.update_value()
        painter.drawText(self.from_point, f"{self._name} (value={self._value})")

        
    # Собирает точки для конкретной связи
    def _parse_link_to_points(self):
        p1, p2s = None, []
        margin = 50
        
        if not ConnectionManager().exists(self._name):
            return p1, p2s
        
        link = ConnectionManager().get_instance(self._name)
        if DrawnItemsManager().system_exists(link.from_system):
            system_item = DrawnItemsManager().get_system(link.from_system)

            i_port = system_item.output_port(self.name)
            if i_port != None:
                p1 = system_item.mapToParent(i_port.center)
                # print(f"Signal={self.name} From=({p1.x()}, {p1.y()}), To={p2s}")

        for to_system in link.to_systems:
            if DrawnItemsManager().system_exists(to_system):
                system_item = DrawnItemsManager().get_system(to_system)

                i_port = system_item.input_port(self.name)
                if i_port != None:
                    p2 = system_item.mapToParent(i_port.center)
                    p2s.append(p2)

        if p1 is None:
            p1 = QPointF()
            p1.setX(min([p.x() for p in p2s]) - margin) # Left
            p1.setY(min([p.y() for p in p2s])) # Top
            
        if not p2s:
            p2s.append(p1 + QPointF(margin, 0))

        return p1, p2s