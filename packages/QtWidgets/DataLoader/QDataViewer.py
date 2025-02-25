from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from PyQt6.QtWebEngineWidgets import QWebEngineView


import pandas as pd
import numpy as np 

import plotly
import plotly.graph_objects as go

from packages.Utils.DBStorage import DBStorage



class QDataViewer(QWebEngineView):
    
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        self.__plot = go.Figure()
        self.__update_plot()

        
    def __update_plot(self):
        self.setHtml(self.__plot.to_html(include_plotlyjs='cdn'))

    
    def __set_plot(self, name : str):
        self.__plot.add_trace(go.Scatter(y=DBStorage.find(name).to_numpy(), mode="lines", name=name))
    
    def __remove_plot(self, name : str):
        # self.__plot.data = [trace for trace in self.__plot.data if trace.name is not name]
        # self.__plot[name].clear()
        # TODO
        pass
    

    def update_plot_state(self, name : str, enable : bool):
        if (enable): 
            self.__set_plot(name)
        else: 
            self.__remove_plot(name)
        self.__update_plot()
        
    def redraw_table(self):
        if DBStorage().empty():
            return
        
        # df = DBStorage().data()
        
        # fig = go.Figure(data=go.Scatter(y=df.to_numpy()))
        # fig.write_html('first_figure.html', auto_open=False)
        # path = QDir.current().filePath('first_figure.html') 
        # url = QUrl.fromLocalFile(path)
        # self.view.load(url)