from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from .Items import *
from .QSignalsList import QSignalList

from packages.SystemModule.Connection import ConnectionManager

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
    
    
    def create_system(self):
        if not self.__get_name():
            self.incorrect_system_parameters.emit("System name empty")
            return
        
        self.create_button_pressed.emit(self.__get_system_attributes())
    
    
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
    
    
    def __get_checked_inputs(self):
        return self.__signals_list
    
    
    def __get_number_outputs(self):
        # return self.__output_number_edit.value()
        return 0
    
    
    def __get_system_attributes(self):
        return dict(name=self.__get_name(), 
                    inputs=self.__get_checked_inputs(),
                    outputs=self.__get_number_outputs())
        
    def __create_signal(self):
        dialog = QSignalAdder()
        dialog.signal_created.connect(lambda name : self.update_parameters_list([name]))
        
        dialog.exec()
