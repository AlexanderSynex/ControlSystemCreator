from PyQt6.QtWidgets import QFrame, QGroupBox

class QSystemSelector(QGroupBox):
    def __init__(self, parent=None):
        super().__init__("System Selector", parent)
        