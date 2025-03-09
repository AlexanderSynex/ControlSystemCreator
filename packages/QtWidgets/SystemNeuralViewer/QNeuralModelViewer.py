from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from PyQt6.QtWebEngineWidgets import QWebEngineView

from PIL.ImageQt import ImageQt
from io import BytesIO
import html
import visualkeras as vk


from packages.SystemModule.System import SystemManager

class QNeuralModelViewer(QGraphicsView):
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        self.__scene = QGraphicsScene()
        self.setScene(self.__scene)
    
    def clear(self):
        self.__scene.clear()
        
    def show(self, system_name):
        if not SystemManager().exists(system_name):
            return
        pass
        self.clear()
        system = SystemManager().get_instance(system_name)
        img = ImageQt(vk.layered_view(system.model
                                      , legend=True
                                      , show_dimension=True
                                      , min_xy=min(self.size().width(), self.size().height()) / 2
                                      , scale_z=0.5
                                      )
                      )
        self.__scene.addPixmap(QPixmap.fromImage(img))
