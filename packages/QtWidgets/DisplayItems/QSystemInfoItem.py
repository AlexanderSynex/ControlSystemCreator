from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class QSystemInfoItem(QListWidgetItem):
    
    def __init__(self, system, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.system = system