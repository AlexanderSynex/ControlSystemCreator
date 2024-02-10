from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from packages import ConnectionManager

class QSignalAdder(QDialog):
    
    signal_created = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__init_UI()
        
        self.__button_box.accepted.connect(self.__create_system)
        self.__button_box.rejected.connect(self.close)

        
    def __init_UI(self):
        layout = QVBoxLayout()
        
        self.__name_edit = QLineEdit()
        self.__value_edit = QDoubleSpinBox()
        self.__button_box = QDialogButtonBox()
        
        regex = QRegularExpression("^[a-zA-Z][a-zA-Z0-9]+")
        validator = QRegularExpressionValidator(regex)
        self.__name_edit.setValidator(validator)
        
        name_layout = QHBoxLayout()
        name_layout.addWidget(QLabel("Name"), 1)
        name_layout.addWidget(self.__name_edit, 5)
        
        value_layout = QHBoxLayout()
        value_layout.addWidget(QLabel("Value"), 1)
        value_layout.addWidget(self.__value_edit, 5)
        
        self.__button_box.addButton("Add", QDialogButtonBox.ButtonRole.AcceptRole)
        self.__button_box.addButton("Close", QDialogButtonBox.ButtonRole.RejectRole)
        
        layout.addLayout(name_layout)
        layout.addLayout(value_layout)
        layout.addWidget(self.__button_box)
        
        self.setLayout(layout)
        
    def __create_system(self):
        name = self.__name_edit.text()
        value = self.__value_edit.value()
        
        print(name, value)
        
        if (ConnectionManager().exists(name)):
            print("Signal already exists")
            self.close()
            return
            
        ConnectionManager().get_instance(name=name, 
                                         value=value)
        
        self.signal_created.emit(name)