from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class QSystemDrawElement(QGraphicsRectItem):
    def __init__(self):
        super().__init__(0, 0, 50, 50)