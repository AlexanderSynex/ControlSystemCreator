from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from .Items import *
from .QSignalsList import QSignalList

from packages.SystemModule.System import SystemManager

class QParametersEditor(QGroupBox):
    
    create_button_pressed = pyqtSignal(dict)
    incorrect_system_parameters = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super().__init__("Parameters Editor")
        
        self.__init_UI()
        
        
    def __init_UI(self):
        __layout = QVBoxLayout()
        
        __name_label = QLabel("Имя системы")
        self.__name_edit  = QLineEdit()
        regex = QRegularExpression("^[a-zA-Z][a-zA-Z0-9]+")
        validator = QRegularExpressionValidator(regex)
        self.__name_edit.setValidator(validator)
        
        __input_gb = QGroupBox("Входные сигналы")
        __input_layout = QVBoxLayout()
        self.__signals_list = QSignalList()
        
        
        self.__add_button = QPushButton("Add signal")
        __input_layout.addWidget(self.__add_button)
        self.__add_button.clicked.connect(self.__create_signal)
        
        __input_layout.addWidget(self.__signals_list)
        __input_gb.setLayout(__input_layout)
        
        __io_layout = QVBoxLayout()
        __io_layout.addWidget(__input_gb)
        
        __create_button = QPushButton("Создать систему")
        
        __layout.addWidget(__name_label)
        __layout.addWidget(self.__name_edit)
        
        __layout.addLayout(__io_layout)
        
        __layout.addWidget(__create_button)
        
        __create_button.clicked.connect(self.create_system)
        
        self.setLayout(__layout)
    
    
    def __is_correct_system_configuration(self) -> bool:
        return self.__get_name() and self.__get_checked_inputs() and self.__get_checked_outputs()
    
    
    def create_system(self):
        if not self.__is_correct_system_configuration():
            faults = []
            if not self.__get_name(): faults.append('System name')
            if not self.__get_checked_inputs(): faults.append('Inputs')
            if not self.__get_checked_outputs(): faults.append('Outputs')
            self.incorrect_system_parameters.emit(f"Incorrect system configuration. Not specified: {', '.join(faults)}")
            return
        
        self.create_button_pressed.emit(self.__get_system_attributes())
    
    def display_clear(self):
        self.__name_edit.setText("")
        self.__signals_list.uncheck()
    
    def clear(self):
        self.clear_parameters_list()
        self.__name_edit.setText("")
        self.__signals_list.uncheck()
        
    
    def clear_parameters_list(self):
        self.__signals_list.clear()
    
    
    def update_parameters_list(self, parameters):
        for parameter in parameters:
            self.__signals_list.add(parameter=parameter)
            
    
    
    def __get_name(self):
        return self.__name_edit.text()
    
    
    def __get_checked_inputs(self) -> list:
        return self.__signals_list.checked_inputs()
    
    
    def __get_checked_outputs(self) -> list:
        return self.__signals_list.checked_outputs()
        
    
    def __get_system_attributes(self):
        return dict(name=self.__get_name(), 
                    inputs=self.__get_checked_inputs(),
                    outputs=self.__get_checked_outputs())
        
        
    def __create_signal(self):
        dialog = QSignalAdder()
        dialog.signal_created.connect(lambda name : self.update_parameters_list([name]))
        
        dialog.exec()
        
        
    def display_parameters(self, system_name : str):
        if not SystemManager().exists(name=system_name):
            return
        system = SystemManager().get_instance(name=system_name)
        self.display_clear()
        self.__name_edit.setText(system.name)
        self.__signals_list.display_checked(inputs=system.input_keys, outputs=system.output_keys)