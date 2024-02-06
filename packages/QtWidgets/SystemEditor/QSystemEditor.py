from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from .QSystemSelector import QSystemSelector
from .QParametersEditor import QParametersEditor

from packages.QtWidgets.SystemViewer import QSystemViewer

from .Items import QSystemInfo

from packages.SystemModule.Connection import (ConnectionManager, 
                                              ConnectionDataWrapper)

from packages.SystemModule.System import (SystemManager, 
                                          SystemDataWrapper)



class QSystemEditor(QWidget):
    system_created = pyqtSignal(str)
    systems_loaded = pyqtSignal()
    
    system_error = pyqtSignal(str)
    
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.__init_UI()
    
    
    def __init_UI(self):
        self.__layout = QHBoxLayout()
        
        self.__parameters_edit = QParametersEditor()
        self.__parameters_edit.create_button_pressed.connect(self.__create_system)
        self.__parameters_edit.incorrect_system_parameters.connect(self.system_error)
        self.__layout.addWidget(self.__parameters_edit, 4)
        
        self.__system_selector = QSystemSelector()
        __selector_container = QGroupBox("Created systems")
        __selector_layout = QHBoxLayout(__selector_container)
        __selector_layout.addWidget(self.__system_selector)
        
        self.__layout.addWidget(__selector_container, 1)
        self.setLayout(self.__layout)
        
        
    def __create_system(self, params):
        name = params['name']
        input_names = params['inputs']
        output_number = params['outputs']
        
        if SystemManager().exists(name):
            self.system_error.emit(f"System {name} already exists")
            return
        
        ConnectionManager().get_instances(names=input_names)
        output_names = ConnectionManager().create_internal_connections(output_number)
        
        sys = SystemManager().get_instance(name=name,
                                           Inputs=input_names,
                                           Outputs=output_names)
        
        if sys is None:
            self.system_error.emit(f"System {name} can not be created")
            return
        
        self.system_created.emit(name)
        
        self.update_parameters(output_names)
        self.__system_selector.add_system(sys.name)
    
    
    def update_parameters(self, loaded_names):
        self.__parameters_edit.update_parameters_list(loaded_names)
    
    
    def clear(self):
        self.__system_selector.clear()
        
        
    def update(self):
        self.clear()
        self.__system_selector.add_systems(SystemManager().get_keys())
        
        self.__parameters_edit.clear_parameters_list()
        self.__parameters_edit.update_parameters_list(ConnectionManager().get_keys())