from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from  packages.SystemModule.Singleton import Singleton
from  packages.SystemModule import (ConnectionManager, SystemManager)

from .QSystemDrawElement import QSystemDrawElement
from .QSignalDrawElement import QSignalDrawElement

class SystemDrawingManager(metaclass=Singleton):
    __margin = 10 # px
    __positions = {0 : []} # index inside weigths
    __draw_items = {}
    __canvas = None
    
    
    def __clear(cls):
        cls.__positions = {0 : []}
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
                cls.__draw_items[system] = draw_item
                cls.__canvas.add(draw_item)
                
    
    def __draw_connections(cls):
        pass
        
    
    def draw(cls):
        cls.__load_systems()
        
        cls.__draw_systems()
        # cls.__draw_connections()
