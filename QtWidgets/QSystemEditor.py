from PyQt6.QtWidgets import QWidget, QGroupBox, QHBoxLayout

from .QSystemSelector import QSystemSelector
from .QParametersEditor import QParametersEditor

class QSystemEditor(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.init_UI()
    
    
    def init_UI(self):
        self.__window = QWidget()
        self.__layout = QHBoxLayout()
        self.__layout.addWidget(QParametersEditor(), 1)
        self.__layout.addWidget(QSystemSelector(), 0)
        self.setWindowTitle("System Editor")
        self.setLayout(self.__layout)
