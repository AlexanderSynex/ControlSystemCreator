from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from packages.QtWidgets import QSystemEditor, QSystemViewer
from packages.QtWidgets.SystemViewer.DrawingElements import SystemDrawingManager

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        tab = QTabWidget(self)
        viewer = QSystemViewer()
        editor = QSystemEditor()
        
        tab.addTab(editor, "Editor")
        tab.addTab(viewer, "Viewer")
        
        editor.system_created.connect(viewer.update)
        editor.systems_loaded.connect(viewer.update)
        
        self.setCentralWidget(tab)
        
        self.__init_menu_bar()
        
    
    def __init_menu_bar(self):
        __file_menu = self.menuBar().addMenu("File")
        
        load_links_action = QAction("Load inputs", self)
        load_links_action.setShortcut(QKeySequence("Ctrl+O"))
        __file_menu.addAction(load_links_action)
        
        
        load_system_action = QAction("Load systems", self)
        load_system_action.setShortcut(QKeySequence("Ctrl+Shift+O"))
        __file_menu.addAction(load_system_action)
        
        
        save_system_action = QAction("Save systems", self)
        save_system_action.setShortcut(QKeySequence("Ctrl+S"))
        __file_menu.addAction(save_system_action)
        
        # load_links_action.triggered.connect(self.__load__input_links_action)
        # load_system_action.triggered.connect(self.__load_systems_action)
        # save_system_action.triggered.connect(self.__save_systems_action)
        
        load_links_action.triggered.connect(lambda: print("load action"))
        load_system_action.triggered.connect(lambda: print("load action"))
        save_system_action.triggered.connect(lambda: print("save action"))
        
    
    
    def __clear_status(self):
        self.__status_bar_label.setText("")
    
    
    def __show_success_status(self, message):
        self.__status_bar_label.setText(f"<b>SUCCESS</b>: {message}")
    
    
    def __show_error_status(self, message):
        self.__status_bar_label.setText(f"<b>ERROR</b>: {message}")
