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
        
        self.setUrl(QUrl('https://google.com'))

    def redraw_table(self):
        if DBStorage().empty():
            return
        
        df = DBStorage().data()
        
        fig = go.Figure(data=go.Scatter(y=df.to_numpy()))
        fig.write_html('first_figure.html', auto_open=False)
        path = QDir.current().filePath('first_figure.html') 
        url = QUrl.fromLocalFile(path)
        self.view.load(url)