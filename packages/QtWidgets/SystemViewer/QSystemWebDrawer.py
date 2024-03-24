from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWebEngineWidgets import *

class QSystemWebDrawer(QWebEngineView):
    def __init__(self):
        super().__init__()
        
        self.setUrl(QUrl("http://google.com"))
        # self.show()