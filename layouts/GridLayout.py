import sys
import os
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QWidget

class Demo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        layout = QGridLayout()        
        layout.setGeometry(QRect(50,50,400,400))      
        layout.addWidget(QLabel('Label 0,0'),0,0)        
        layout.addWidget(QLabel('Label 0,1'),0,1)
        layout.addWidget(QLabel('Label 1,0'),1,0)
        layout.addWidget(QLabel('Label 1,1'),1,1) 

        self.setLayout(layout) 

def runDemo(parent):
    wigdet =  Demo(parent)
    return wigdet