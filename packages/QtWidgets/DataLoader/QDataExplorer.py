from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from .QDataController import QDataController
from .QDataViewer import QDataViewer

from packages.Utils.DBStorage import DBStorage

class QDataExplorer(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.__init_UI()


    def __init_UI(self):
        self.__layout = QHBoxLayout()

        self.__plotter = QDataViewer()
        self.__control = QDataController()

        self.__layout.addWidget(self.__plotter, 2)
        self.__layout.addWidget(self.__control, 0)
        
        self.__control.db_path_recieved.connect(self.__load_csv_data)
        self.__control.plot_changed.connect(self.__plotter.update_plot_state)
        
        self.setLayout(self.__layout)
        
        self.__control.load()
        
        

    def __load_csv_data(self, path : str):
        print('here')
        if DBStorage.load(path):
            self.__plotter.redraw_table()
            self.__control.update(DBStorage.titles())