from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

class QParametersEditor(QGroupBox):
    def __init__(self, parent=None):
        super().__init__("Parameters Editor")
        
        self.__init_UI()
        
    def __init_UI(self):        
        __layout = QVBoxLayout()
        
        __name_label = QLabel("Имя системы")
        __name_edit  = QLineEdit()
        
        
        __input_gb = QGroupBox("Входные сигналы")
        __input_layout = QVBoxLayout()
        self.__input_lw = QListWidget()
        
        __input_layout.addWidget(self.__input_lw)
        __input_gb.setLayout(__input_layout)
        
        __output_gb = QGroupBox("Выходные сигналы")
        __output_layout = QVBoxLayout()
        __output_lw = QListWidget()
        __output_layout.addWidget(__output_lw)
        __output_gb.setLayout(__output_layout)
        
        __io_layout = QHBoxLayout()
        __io_layout.addWidget(__input_gb)
        __io_layout.addWidget(__output_gb)
        
        __final_layout = QGridLayout()
        __final_name = QLabel("Получаемая система")
        __overview_tb = QTextBrowser()
        __create_button = QPushButton("Создать систему")
        
        __layout.addWidget(__name_label)
        __layout.addWidget(__name_edit)
        
        __layout.addLayout(__io_layout)
        
        __final_layout.addWidget(__final_name, 0, 0, 1, 1)
        __final_layout.addWidget(__overview_tb, 1, 0, 2, 1)
        __final_layout.addWidget(__create_button, 1, 1, 2, 1)
        
        __layout.addLayout(__final_layout)
        
        self.setLayout(__layout)
        
    def update_parameters_list(self, parameters):
        for parameter in parameters:
            item = QListWidgetItem(parameter)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
            item.setCheckState(Qt.CheckState.Unchecked)
            self.__input_lw.addItem(item)