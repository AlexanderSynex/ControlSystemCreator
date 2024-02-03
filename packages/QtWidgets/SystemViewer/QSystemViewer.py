from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from .QConnectionList import QConnectionList
from .QSystemDrawer import QSystemDrawer

from .DrawingElements import QSystemDrawElement, QSignalDrawElement
from .DrawingElements import SystemDrawingManager

from packages.SystemModule.Connection import (ConnectionManager, 
                                              ConnectionDataWrapper)

from packages.SystemModule.System import (SystemManager,
                                          SystemDataWrapper)


class QSystemViewer(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        
        self.__init_UI()
        
    
    def __init_UI(self):
        self.__window = QWidget()
        self.__layout = QHBoxLayout()
        
        self.__signals_container = QGroupBox("Signals list")
        __signals_layout = QHBoxLayout()
        self.__signals_lw = QConnectionList()
        __signals_layout.addWidget(self.__signals_lw)
        self.__signals_container.setLayout(__signals_layout)
        
        
        self.__graph_container = QGroupBox("System image")
        __graph_layout = QHBoxLayout()
        self.__graph_view = QSystemDrawer()
        __graph_layout.addWidget(self.__graph_view)
        self.__graph_container.setLayout(__graph_layout)
        
        self.__layout.addWidget(self.__signals_container, 0)
        self.__layout.addWidget(self.__graph_container, 1)
        
        self.__window.setLayout(self.__layout)
        self.setCentralWidget(self.__window)
        self.setWindowTitle("System Editor")
        
        self.__init_menu_bar()
        
        SystemDrawingManager().set_canvas(self.__graph_view)
        
    
    def __init_menu_bar(self):
        __file_menu = self.menuBar().addMenu("File")
        
        load_system_action = QAction("Load systems", self)
        load_system_action.setShortcut(QKeySequence("Ctrl+Shift+O"))
        __file_menu.addAction(load_system_action)
        
        load_system_action.triggered.connect(self.__load_systems_action)
        
    
    def __load_systems_action(self):
        # fileName, _ = QFileDialog().getOpenFileName(self,
        #                                             caption="Load systems info",
        #                                             directory=QDir().homePath(), 
        #                                             filter="JavaScript Object Notation Files (*.json)")
        
        fileName = "./Data/system_test_no_system_weights.json"
        
        if not fileName:
            self.__show_error_status("No systems loaded")
            return
        
        SystemManager().clear()
        self.__signals_lw.clear()
        
        SystemDataWrapper().from_json(path=fileName)
        self.__signals_lw.add_signals(ConnectionManager().get_keys())
        
        # SystemManager().get_instance("system", ["in1", "in2"], ["out1", "out2", "out3"])
        
        # draw_item = QSystemDrawElement("system")
        # self.__graph_view.add(draw_item)
        
        SystemDrawingManager().draw()
        
        # for in_p1 in draw_item.input_points:
        #     in_p2 = QPointF(in_p1) - QPointF(15, 0)
        #     line_item = QSignalDrawElement(in_p1, in_p2)
        #     self.__graph_view.add(line_item)
            
        # for in_p1 in draw_item.output_points:
        #     in_p2 = QPointF(in_p1) + QPointF(15, 0)
        #     line_item = QSignalDrawElement(in_p1, in_p2)
        #     self.__graph_view.add(line_item)