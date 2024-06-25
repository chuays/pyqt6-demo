import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QWidget

class Demo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.resize(400,300)
        layout = QHBoxLayout()    
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)   
        label=QLabel('Python')     
        label.setStyleSheet('background-color:red;')

        layout.addWidget(label)        
        layout.addWidget(QLabel('Java'))
        layout.addWidget(QLabel('Go'))

        self.setLayout(layout) 

def runDemo(parent):
    wigdet =  Demo(parent)
    return wigdet