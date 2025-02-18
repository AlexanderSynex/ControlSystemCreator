from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class QDataController(QWidget):

    db_path_recieved = pyqtSignal(str)

    def __init__(self, parent = None):    
        super().__init__(parent)

        self.__init_UI()
    

    def __init_UI(self):
        self.__layout = QVBoxLayout()
        self.__load_button = QPushButton('Load')

        self.__layout.addWidget(self.__load_button,0)
        self.__layout.addWidget(QFrame(), 1)

        self.setLayout(self.__layout)

        self.__load_button.clicked.connect(self.__load_db)

    def __load_db(self):
        fileName, _ = QFileDialog().getOpenFileName(parent=self,
                                                    caption="Load csv data",
                                                    directory=QDir().currentPath(), 
                                                    filter="Comma Separated Values (*.csv)")
        
        # fileName = "./Data/db.csv"
        
        if not fileName:
            return

        self.db_path_recieved.emit(fileName)