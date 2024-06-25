import sys
import os
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QWidget,QSizePolicy
from PyQt6 import  QtGui

class Demo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        cb = QRadioButton('Radio Button',self)        
        cb.clicked.connect(self.onClicked)
        layout.addWidget(QLabel('1、标准RadioButton'))
        layout.addWidget(cb)

        groupBox = QGroupBox('2、互斥RadioButtons')        
        self.groupExclusive = QButtonGroup()
        self.groupExclusive.setExclusive(True)        
        groupLayout = QVBoxLayout()

        cb = QRadioButton('RadioButton1',self,objectName='RadioButton1')        
        groupLayout.addWidget(cb)
        self.groupExclusive.addButton(cb)

        cb = QRadioButton('RadioButton2',self,objectName='RadioButton2')        
        groupLayout.addWidget(cb)
        self.groupExclusive.addButton(cb)

        cb = QRadioButton('RadioButton3',self,objectName='RadioButton3')        
        groupLayout.addWidget(cb)
        self.groupExclusive.addButton(cb)
        self.groupExclusive.buttonClicked.connect(self.onGroupClicked)

        groupBox.setLayout(groupLayout)
        layout.addWidget(groupBox)        


        self.setLayout(layout)

    def onClicked(self,event):            
        self.parent.showMessage(f'RadioButton Clicked,isChecked:{event}')

    def onGroupClicked(self,event):
        self.parent.showMessage(f'Exclusive {self.groupExclusive.checkedButton().text()} Clicked,isChecked:{self.groupExclusive.checkedButton().isChecked()}')

    
        

def runDemo(parent):
    wigdet =  Demo(parent)
    return wigdet


class Ui_Form(QWidget):
    def __init__(self):
        super(Ui_Form,self).__init__()
        self.setupUi(self)


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(310, 258)
        self.formLayoutWidget = QWidget(parent=Form)
        self.formLayoutWidget.setGeometry(QRect(52, 84, 231, 91))
        self.formLayoutWidget.setObjectName("formLayoutWidget")

        self.demoPage = runDemo(self) 

    def showMessage(self,msg):
        print(msg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Ui_Form()    
    main.show()    
    #main.showMaximized()
    sys.exit(app.exec())