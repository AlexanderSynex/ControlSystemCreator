from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class QSystemSelector(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        