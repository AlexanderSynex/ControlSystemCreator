from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from packages.SystemModule.Connection import ConnectionManager


class QConnectionItemWidget(QWidget):
    value_changed = pyqtSignal(str)
    def __init__(self, signal_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.signal_name = signal_name
        
        self.__init_UI()
        
        self.__isChanged = False
        
        
    def __init_UI(self):
        self.__layout = QHBoxLayout(self)
        
        self.__name_label = QLabel()        
        self.__value_edit = QDoubleSpinBox()
        
        self.__layout.addWidget(self.__name_label, 2)
        self.__layout.addWidget(self.__value_edit, 4)
        
        self.__value_edit.installEventFilter(self)
        
        self.update_system_info()
        
        self.__value_edit.valueChanged.connect(self.__setChanged)
        
    
    def update_system_info(self):
        
        if not ConnectionManager().exists(self.signal_name):
            return
        
        link = ConnectionManager().get_instance(self.signal_name)
        
        self.__name_label.setText(f"{link.name}")
        self.__value_edit.setValue(link.value)
        
        
    def eventFilter(self, widget, event):
        if (event.type() == QEvent.Type.KeyPress):
            key = event.key()
            if key == Qt.Key.Key_Return or key == Qt.Key.Key_Enter:
                if ConnectionManager().exists(self.signal_name):
                    ConnectionManager().get_instance(self.signal_name).value = self.__value_edit.value()
                    self.value_changed.emit(self.signal_name)
                    self.__isChanged = False
                    self.__updateField()
                return True
        return QWidget.eventFilter(self, widget, event)
    
    def __setChanged(self):
        self.__isChanged = True
        self.__updateField()
    
    
    def __updateField(self):
        self.__value_edit.setSuffix("")
        if self.__isChanged:
            self.__value_edit.setSuffix(" (unsaved)")