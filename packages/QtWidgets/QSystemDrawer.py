from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class QSystemDrawer(QGraphicsView):
    def __init__(self):
        super().__init__()
        
        self.__scene = QGraphicsScene()
        self.setScene(self.__scene)