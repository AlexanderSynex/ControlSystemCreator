from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from .QSystemSelector import QSystemSelector
from .QParametersEditor import QParametersEditor

from ..SystemModule import ConnectionManager
from ..SystemModule import SystemManager

from .DisplayItems import QSystemInfoItem

class QSystemEditor(QMainWindow):
    
    system_created = pyqtSignal(object)
    
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
        
        self.__system_selector = QSystemSelector()
        __selector_container = QGroupBox("System selector")
        __selector_layout = QHBoxLayout(__selector_container)
        __selector_layout.addWidget(self.__system_selector)
        
        self.__layout.addWidget(__selector_container, 1)
        self.__window.setLayout(self.__layout)
        self.setCentralWidget(self.__window)
        self.setWindowTitle("System Editor")
        
        self.__status_bar_label = QLabel()
        self.statusBar().addWidget(self.__status_bar_label)
        self.__clear_status()
        
        
    def __create_system(self, params):
        name = params['name']
        input_names = params['inputs']
        output_number = params['outputs']
        
        self.__clear_status()
        if SystemManager().exists(name):
            self.__show_error_status(f"System {name} already exists")
            return
        
        inputs = ConnectionManager().get_instances(names=input_names)
        outputs = ConnectionManager().create_internal_connections(output_number)
        
        sys = SystemManager().get_instance(name=name,
                                           Inputs=inputs,
                                           Outputs=outputs)
        
        if sys is None:
            self.__show_error_status(f"System {name} can not be created")
            return
        
        self.__show_success_status(f"System {name} created")
        self.system_created.emit(sys)
        
        links = []
        for link in outputs:
            links.append(link.get_name())
        
        self.__parameters_edit.update_parameters_list(links)
        
        self.__system_selector.addItem(QSystemInfoItem(system=sys))
        
        sys.print()


    def __load__input_links_action(self):
        # fileName, _ = QFileDialog.getOpenFileName(self, 
        #                                        caption="Load inputs", 
        #                                        directory=QDir().homePath(), 
        #                                        filter="Comma-Separated Files (*.csv)")
        
        fileName = "./Data/file1.csv"
        
        if not fileName:
            self.__show_error_status("No parameters loaded")
            return
        
        ConnectionManager().clear()
        ConnectionManager().load_from_csv(fileName)
        
        links = ConnectionManager().get_keys()
        
        if not links:
            self.__show_error_status("No parameters loaded")
        self.__show_success_status(f"Loaded {len(links)} parameters")
        
        self.__parameters_edit.clear_parameters_list()
        self.__parameters_edit.update_parameters_list(links)
        
    
    def __clear_status(self):
        self.__status_bar_label.setText("")
    
    
    def __show_success_status(self, message):
        self.__status_bar_label.setText(f"<b>SUCCESS</b>: {message}")
    
    
    def __show_error_status(self, message):
        self.__status_bar_label.setText(f"<b>ERROR</b>: {message}")