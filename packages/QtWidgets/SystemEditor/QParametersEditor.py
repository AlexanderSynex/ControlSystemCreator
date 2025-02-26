from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from .Items import *

import packages.SystemModule.System.SystemManager

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
        self.__input_lw = QListWidget()
        
        self.__add_button = QPushButton("Add signal")
        __input_layout.addWidget(self.__add_button)
        self.__add_button.clicked.connect(self.__create_signal)
        
        __input_layout.addWidget(self.__input_lw)
        __input_gb.setLayout(__input_layout)
        
        __output_gb = QGroupBox("Выходные сигналы")
        __output_layout = QHBoxLayout()
        self.__output_number_edit = QSpinBox()
        self.__output_number_edit.setMinimum(1)
        __output_number_name = QLabel("Количество сигналов")
        __output_number_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        __output_layout.addWidget(__output_number_name, 0)
        __output_layout.addWidget(self.__output_number_edit, 1)
        __output_gb.setLayout(__output_layout)
        
        __io_layout = QVBoxLayout()
        __io_layout.addWidget(__input_gb)
        __io_layout.addWidget(__output_gb)
        
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
        self.__output_number_edit.setValue(self.__output_number_edit.minimum())
        
    
    def clear_parameters_list(self):
        self.__input_lw.clear()
    
    
    def update_parameters_list(self, parameters):
        for parameter in parameters:
            item = QLinkItem(parameter)

            self.__input_lw.addItem(item)
    
    
    def __get_name(self):
        return self.__name_edit.text()
    
    
    def __get_checked_inputs(self):
        signals = []
        for row_i in range(self.__input_lw.count()):
            item = self.__input_lw.item(row_i)
            if item.checkState() == Qt.CheckState.Checked:
                signals.append(item.text())
        
        return signals
    
    
    def __get_number_outputs(self):
        return self.__output_number_edit.value()
    
    
    def __get_system_attributes(self):
        return dict(name=self.__get_name(), 
                    inputs=self.__get_checked_inputs(),
                    outputs=self.__get_number_outputs())
        
    def __create_signal(self):
        dialog = QSignalAdder()
        dialog.signal_created.connect(lambda name : self.update_parameters_list([name]))
        
        dialog.exec()
        
        