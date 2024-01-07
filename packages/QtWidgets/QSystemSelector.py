from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class QSystemSelector(QGroupBox):
    def __init__(self, parent=None):
        super().__init__("System Selector", parent)
        