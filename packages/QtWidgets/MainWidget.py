from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from packages.QtWidgets import QSystemEditor, QSystemViewer
from packages.QtWidgets.SystemViewer.DrawingElements import SystemDrawingManager

class MainWidget(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        
        viewer = QSystemViewer()
        editor = QSystemEditor()
        
        self.addTab(editor, "Editor")
        self.addTab(viewer, "Viewer")
        
        
        editor.system_created.connect(viewer.update)
        editor.systems_loaded.connect(viewer.update)