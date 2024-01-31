from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from  packages.SystemModule.Singleton import Singleton
from  packages.SystemModule import (ConnectionManager, SystemManager)

from .QSystemDrawElement import QSystemDrawElement
from .QSignalDrawElement import QSignalDrawElement

from .DrawnItemsManager import DrawnItemsManager

class SystemDrawingManager(metaclass=Singleton):
    __x_margin, __y_margin = 100, 50 # px
    __positions = {0 : []} # index inside weigths
    __canvas = None
    
    
    def __clear(cls):
        cls.__positions = {0 : []}
        DrawnItemsManager().clear()
        __draw_items = {}
    
    
    def set_canvas(cls, canvas):
        cls.__canvas = canvas
    
    
    def __load_systems(cls):
        cls.__clear()
        
        for system_name in SystemManager().get_keys():
            system = SystemManager().get_instance(system_name)
            
            if system.weight not in cls.__positions:
                cls.__positions[system.weight] = []
                
            if system_name not in cls.__positions[system.weight]:
                cls.__positions[system.weight].append(system_name)
    
    
    def __draw_systems(cls):
        for column in cls.__positions:
            for i, system in enumerate(cls.__positions[column]):
                draw_item = QSystemDrawElement(name=system)

                w = draw_item.boundingRect().width()
                h = draw_item.boundingRect().height()

                draw_item.moveBy((w + cls.__x_margin) * column,
                                 (h + cls.__y_margin) * i)

                DrawnItemsManager().add_system(draw_item)
                cls.__canvas.add(draw_item)
                
    
    def __draw_connections(cls):
        # Для каждой системы на холсте
        for name in DrawnItemsManager().systems:
            system = DrawnItemsManager().get_system(name)
            # Для каждого выходного порта
            for port in system.output_ports:
                # Создать сигнал и отобрзить его
                signal_item = QSignalDrawElement(port.name)
                cls.__canvas.add(signal_item)


    def draw(cls):
        cls.__load_systems()
        
        cls.__draw_systems()
        cls.__draw_connections()



