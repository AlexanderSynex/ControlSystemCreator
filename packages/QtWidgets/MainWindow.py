from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from packages.QtWidgets import QSystemEditor, QSystemViewer, QDataExplorer
from packages.QtWidgets.SystemViewer.DrawingElements import SystemDrawingManager
from packages.QtWidgets.SystemViewer.DrawingElements.DrawnItemsManager import DrawnItemsManager

from packages.SystemModule.Connection import (ConnectionManager, 
                                              ConnectionDataWrapper)

from packages.SystemModule.System import (SystemManager, 
                                          SystemDataWrapper)

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        # tab = QTabWidget(self)
        # self.__viewer = QSystemViewer()
        # self.__editor = QSystemEditor()
        self.__data_explorer = QDataExplorer(self)
        self.setCentralWidget(self.__data_explorer)
        # tab.addTab(self.__editor, "Editor")
        # tab.addTab(self.__viewer, "Viewer")
        # tab.addTab(self.__data_extractor, "Data Inspector")

        # self.__editor.system_created.connect(self.__viewer.redraw)
        # self.__editor.system_created.connect(lambda name: self.__show_success_status(f"System {name} created"))
        # self.__editor.systems_loaded.connect(self.__viewer.redraw)
        # self.__editor.system_error.connect(self.__show_error_status)
        
        # self.setCentralWidget(tab)
        
        self.__init_menu_bar()
        
        self.__status_bar_label = QLabel()
        self.statusBar().addWidget(self.__status_bar_label)
        self.__clear_status()
        
    
    def __init_menu_bar(self):
        __file_menu = self.menuBar().addMenu("File")
        
        new_action = QAction("New", self)
        new_action.setShortcut(QKeySequence("Ctrl+N"))
        __file_menu.addAction(new_action)
        
        load_links_action = QAction("Load inputs", self)
        load_links_action.setShortcut(QKeySequence("Ctrl+O"))
        __file_menu.addAction(load_links_action)
        
        
        load_system_action = QAction("Load systems", self)
        load_system_action.setShortcut(QKeySequence("Ctrl+Shift+O"))
        __file_menu.addAction(load_system_action)
        
        
        save_system_action = QAction("Save systems", self)
        save_system_action.setShortcut(QKeySequence("Ctrl+S"))
        __file_menu.addAction(save_system_action)
        
        
        new_action.triggered.connect(self.__new_systems_action)
        load_links_action.triggered.connect(self.__load__input_links_action)
        load_system_action.triggered.connect(self.__load_systems_action)
        save_system_action.triggered.connect(self.__save_systems_action)
        
    
    def __new_systems_action(self):
        ConnectionManager().clear()
        SystemManager().clear()
        DrawnItemsManager().clear()
        SystemDrawingManager().clear()
        self.__editor.clear()   
        self.__viewer.clear()

    
    def __clear_status(self):
        self.__status_bar_label.setText("")
    
    
    def __show_success_status(self, message):
        self.__status_bar_label.setText(f"<b>SUCCESS</b>: {message}")
    
    
    def __show_error_status(self, message):
        self.__status_bar_label.setText(f"<b>ERROR</b>: {message}")


    def __load__input_links_action(self):
        fileName, _ = QFileDialog.getOpenFileName(parent=self, 
                                                  caption="Load inputs", 
                                                  directory=QDir().currentPath(), 
                                                  filter="Comma-Separated Files (*.csv)")
        
        # fileName = "./Data/file1.csv"
        
        if not fileName:
            self.__show_error_status("No parameters loaded")
            return
        
        loaded_names = ConnectionDataWrapper().load_from_csv(fileName)
        
        if not loaded_names:
            self.__show_error_status("No parameters loaded")
        
        self.__show_success_status(f"Loaded {len(loaded_names)} parameters")
        self.__editor.update_parameters(loaded_names)
        
        self.__viewer.reload_signals()


    def __save_systems_action(self):
        if SystemManager().empty():
            self.__show_error_status("No systems to save")
            return
        
        fileName, _ = QFileDialog().getSaveFileName(self,
                                                    caption="Save systems info",
                                                    #directory=QDir().homePath(), 
                                                    directory=QDir().currentPath(), 
                                                    filter="JavaScript Object Notation Files (*.json)")
        
        if not fileName:
            self.__show_error_status("System saving was canceled")
            return
        
        if '.json' not in fileName:
            fileName += '.json'
        
        file = QFile(fileName)
        if not file.open(QIODevice.OpenModeFlag.WriteOnly | QIODevice.OpenModeFlag.Text):
            self.__show_error_status("File to save could not be opened")
            return
        
        QTextStream(file) << SystemDataWrapper().all_to_json()
        file.close()
        
        self.__show_success_status(f"Systems saved in {fileName}")
        
        
    def __load_systems_action(self):
        fileName, _ = QFileDialog().getOpenFileName(parent=self,
                                                    caption="Load systems info",
                                                    directory=QDir().currentPath(), 
                                                    filter="JavaScript Object Notation Files (*.json)")
        
        fileName = "./Data/system_test_no_system_weights.json"  #TODO
        
        if not fileName:
            self.system_error.emit("No systems loaded")
            return
        
        SystemManager().clear()
        SystemDataWrapper().from_json(path=fileName)
        
        self.__show_success_status(f"Loaded {len(SystemManager().get_keys())} systems")
        
        self.__editor.update()
        self.__viewer.redraw()
        
    
    def update(self):
        self.__editor.update()
        self.__viewer.redraw()
