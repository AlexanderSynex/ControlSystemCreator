from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from .QSystemSelector import QSystemSelector
from .QParametersEditor import QParametersEditor

from ..SystemModule import (ConnectionManager, 
                            ConnectionDataWrapper)
from ..SystemModule import (SystemManager, 
                            SystemDataWrapper)

from .DisplayItems import QSystemInfo

class QSystemEditor(QMainWindow):
    
    system_created = pyqtSignal(object)
    
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.__init_UI()
    
    
    def __init_UI(self):
        self.__window = QWidget()
        self.__layout = QHBoxLayout()
        
        self.__parameters_edit = QParametersEditor()
        self.__parameters_edit.create_button_pressed.connect(self.__create_system)
        self.__parameters_edit.incorrect_system_parameters.connect(self.__show_error_status)
        self.__layout.addWidget(self.__parameters_edit, 4)
        
        self.__system_selector = QSystemSelector()
        __selector_container = QGroupBox("Created systems")
        __selector_layout = QHBoxLayout(__selector_container)
        __selector_layout.addWidget(self.__system_selector)
        
        self.__layout.addWidget(__selector_container, 1)
        self.__window.setLayout(self.__layout)
        self.setCentralWidget(self.__window)
        self.setWindowTitle("System Editor")
        
        self.__status_bar_label = QLabel()
        self.statusBar().addWidget(self.__status_bar_label)
        self.__clear_status()
        
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
        
        load_links_action.triggered.connect(self.__load__input_links_action)
        load_system_action.triggered.connect(self.__load_systems_action)
        save_system_action.triggered.connect(self.__save_systems_action)
        
        
    def __create_system(self, params):
        name = params['name']
        input_names = params['inputs']
        output_number = params['outputs']
        
        self.__clear_status()
        
        if SystemManager().exists(name):
            self.__show_error_status(f"System {name} already exists")
            return
        
        ConnectionManager().get_instances(names=input_names)
        output_names = ConnectionManager().create_internal_connections(output_number)
        
        sys = SystemManager().get_instance(name=name,
                                           Inputs=input_names,
                                           Outputs=output_names)
        
        if sys is None:
            self.__show_error_status(f"System {name} can not be created")
            return
        
        self.__show_success_status(f"System {name} created")
        self.system_created.emit(sys)
        
        self.__parameters_edit.update_parameters_list(output_names)
        self.__system_selector.add_system(sys.name)


    def __load__input_links_action(self):
        # fileName, _ = QFileDialog.getOpenFileName(self, 
        #                                        caption="Load inputs", 
        #                                        directory=QDir().homePath(), 
        #                                        filter="Comma-Separated Files (*.csv)")
        
        fileName = "./Data/file1.csv"
        
        if not fileName:
            self.__show_error_status("No parameters loaded")
            return
        
        loaded_names = ConnectionDataWrapper().load_from_csv(fileName)
        
        if not loaded_names:
            self.__show_error_status("No parameters loaded")
        self.__show_success_status(f"Loaded {len(loaded_names)} parameters")
        
        self.__parameters_edit.update_parameters_list(loaded_names)
        
    
    def __clear_status(self):
        self.__status_bar_label.setText("")
    
    
    def __show_success_status(self, message):
        self.__status_bar_label.setText(f"<b>SUCCESS</b>: {message}")
    
    
    def __show_error_status(self, message):
        self.__status_bar_label.setText(f"<b>ERROR</b>: {message}")
        
    
    def __save_systems_action(self):
        if SystemManager().empty():
            self.__show_error_status("No systems to save")
            return
        
        fileName, _ = QFileDialog().getSaveFileName(self,
                                                    caption="Save systems info",
                                                    directory=QDir().homePath(), 
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
        # fileName, _ = QFileDialog().getOpenFileName(self,
        #                                             caption="Load systems info",
        #                                             directory=QDir().homePath(), 
        #                                             filter="JavaScript Object Notation Files (*.json)")
        
        fileName = "./Data/system_test.json"
        
        if not fileName:
            self.__show_error_status("No systems loaded")
            return
        
        SystemManager().clear()
        SystemDataWrapper().from_json(path=fileName)
        
        self.__system_selector.clear()
        self.__system_selector.add_systems(SystemManager().get_keys())
        self.__show_success_status(f"Loaded {len(SystemManager().get_keys())} systems")
        