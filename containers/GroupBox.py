import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QWidget

class Demo(QWidget):

    def __init__(self,parent=None):
        super(Demo,self).__init__()

        self.parent=parent

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        groupBox= QGroupBox()
        groupBox.setMaximumWidth(300)
        groupBox.setTitle('城市分组')
        layoutCity = QVBoxLayout()
        layoutCity.setAlignment(Qt.AlignmentFlag.AlignTop)
        layoutCity.addWidget(QLabel('北京'))
        layoutCity.addWidget(QLabel('上海'))
        layoutCity.addWidget(QLabel('西安'))
        groupBox.setLayout(layoutCity)
        layout.addWidget(groupBox)

        groupBox= QGroupBox()
        groupBox.setMaximumWidth(300)
        groupBox.setTitle('省份分组')
        groupBox.setCheckable(True)
        layoutCity = QVBoxLayout()
        layoutCity.setAlignment(Qt.AlignmentFlag.AlignTop)
        layoutCity.addWidget(QCheckBox('广东'))
        layoutCity.addWidget(QCheckBox('陕西'))
        layoutCity.addWidget(QCheckBox('江苏'))
        groupBox.setLayout(layoutCity)
        layout.addWidget(groupBox)

        self.setLayout(layout)


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