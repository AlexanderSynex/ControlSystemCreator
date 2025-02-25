from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from .QDataSelector import QDataSelector

class QDataController(QWidget):

    db_path_recieved = pyqtSignal(str)
    plot_changed = pyqtSignal(str, bool)
    
    def __init__(self, parent = None):    
        super().__init__(parent)

        self.__init_UI()
        self.__load_db()
    

    def __init_UI(self):
        self.__layout = QVBoxLayout()
        self.__selector = QDataSelector()
        self.__load_button = QPushButton('Load')

        self.__layout.addWidget(self.__selector, 1)
        self.__layout.addWidget(self.__load_button,0)
        
        self.setLayout(self.__layout)
        
        self.__load_button.clicked.connect(self.__load_db)
        self.__selector.plot_changed.connect(self.plot_changed)
    
    
    def __load_db(self):
        # fileName, _ = QFileDialog().getOpenFileName(parent=self,
        #                                             caption="Load csv data",
        #                                             directory=QDir().currentPath(), 
        #                                             filter="Comma Separated Values (*.csv)")
        
        fileName = "./Data/db_short.csv"
        
        if not fileName:
            return
        
        self.db_path_recieved.emit(fileName)
        
        
    def load(self):
        self.__load_db()
        
        
    def update(self, titles : list):
        self.__selector.display(titles)
        