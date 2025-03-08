from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class QIOCheckGroup(QWidget):
    
    state_changed = pyqtSignal(bool, bool)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__init_UI()
        
    def __init_UI(self):
        self.__layout = QHBoxLayout(self)
        
        self.__input = QCheckBox('Input')
        self.__input.setTristate(False)
        self.__output = QCheckBox('Output')
        self.__output.setTristate(False)
        
        self.__layout.addWidget(self.__input, alignment=Qt.AlignmentFlag.AlignLeft)
        self.__layout.addWidget(self.__output, alignment=Qt.AlignmentFlag.AlignRight)
        
        self.__input.checkStateChanged.connect(lambda state: self.__revert_checkboxes(state, self.__output))
        self.__output.checkStateChanged.connect(lambda state: self.__revert_checkboxes(state, self.__input))
        self.__input.checkStateChanged.connect(lambda _: self.state_changed.emit(self.input(), self.output()))
        self.__output.checkStateChanged.connect(lambda _: self.state_changed.emit(self.input(), self.output()))
    
    def __revert_checkboxes(self, state, opposite : QCheckBox):
        if (state is Qt.CheckState.Checked):
            opposite.setCheckState(Qt.CheckState.Unchecked)
    
    def clear(self):
        self.__input.setCheckState(Qt.CheckState.Unchecked)
        self.__output.setCheckState(Qt.CheckState.Unchecked)
        
    def input(self) -> bool:
        return self.__input.isChecked()
    
    def output(self) -> bool:
        return self.__output.isChecked()