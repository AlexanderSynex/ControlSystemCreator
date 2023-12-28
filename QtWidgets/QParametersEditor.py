from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

class QParametersEditor(QGroupBox):
    def __init__(self):
        super().__init__("Parameters Editor")
        
        self.init_UI()
        
    def init_UI(self):
        self.__layout = QVBoxLayout()
        
        self.__name_label = QLabel("Имя системы")
        self.__name_edit  = QLineEdit()
        
        
        self.__input_gb = QGroupBox("Входные сигналы")
        self.__input_layout = QVBoxLayout()
        self.__input_lw = QListWidget()
        self.__input_layout.addWidget(self.__input_lw)
        self.__input_gb.setLayout(self.__input_layout)
        
        self.__output_gb = QGroupBox("Выходные сигналы")
        self.__output_layout = QVBoxLayout()
        self.__output_lw = QListWidget()
        self.__output_layout.addWidget(self.__output_lw)
        self.__output_gb.setLayout(self.__output_layout)
        
        self.__io_layout = QHBoxLayout()
        self.__io_layout.addWidget(self.__input_gb)
        self.__io_layout.addWidget(self.__output_gb)
        
        self.__final_layout = QGridLayout()
        self.__final_name = QLabel("Получаемая система")
        self.__overview_tb = QTextBrowser()
        self.__create_button = QPushButton("Создать систему")
        
        self.__layout.addWidget(self.__name_label)
        self.__layout.addWidget(self.__name_edit)
        
        self.__layout.addLayout(self.__io_layout)
        
        self.__final_layout.addWidget(self.__final_name, 0, 0, 1, 1)
        self.__final_layout.addWidget(self.__overview_tb, 1, 0, 2, 1)
        self.__final_layout.addWidget(self.__create_button, 1, 1, 2, 1)
        
        self.__layout.addLayout(self.__final_layout)
        
        self.setLayout(self.__layout)