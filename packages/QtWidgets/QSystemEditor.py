from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from .QSystemSelector import QSystemSelector
from .QParametersEditor import QParametersEditor

from ..SystemModule import ConnectionManager

class QSystemEditor(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.__init_UI()
    
    
    def __init_UI(self):
        __file_menu = self.menuBar().addMenu("File")
        __load_action = QAction("Load inputs", self)
        __load_action.setShortcut(QKeySequence("Ctrl+O"))
        __file_menu.addAction(__load_action)
        
        __load_action.triggered.connect(self.__load__input_links_action)
        
        self.__window = QWidget()
        self.__layout = QHBoxLayout()
        
        self.__parameters_edit = QParametersEditor()
        self.__parameters_edit.create_button_pressed.connect(self.__create_system)
        self.__layout.addWidget(self.__parameters_edit, 4)
        self.__layout.addWidget(QSystemSelector(), 1)
        self.__window.setLayout(self.__layout)
        self.setCentralWidget(self.__window)
        self.setWindowTitle("System Editor")
        
        self.statusBar().showMessage("")
        
        
    def __create_system(self):
        print("button pressed")
        
    def __load__input_links_action(self):
        # fileName, _ = QFileDialog.getOpenFileName(self, 
        #                                        caption="Load inputs", 
        #                                        directory=QDir().homePath(), 
        #                                        filter="Comma-Separated Files (*.csv)")
        
        fileName = "./Data/file1.csv"
        
        if not fileName:
            self.statusBar().showMessage("No parameters loaded")
            return
        
        ConnectionManager().load_from_csv(fileName)
        
        links = ConnectionManager().get_instances()
        
        if not links:
            self.statusBar().showMessage("No parameters loaded")
        self.statusBar().showMessage(f"Loaded {len(links)} parameters")
        
        self.__parameters_edit.update_parameters_list(links)