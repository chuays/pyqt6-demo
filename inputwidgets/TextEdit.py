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

        mainLayout = QVBoxLayout()
        scrollArea = QScrollArea(self)
        scrollArea.setWidgetResizable(True)

        widget=QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        textEdit = QTextEdit("Hello World", self)
        textEdit.setFixedSize(QSize(300,30))
        layout.addWidget(QLabel('1、显示文本')) 
        layout.addWidget(textEdit)   

        textEdit = QTextEdit(self)
        textEdit.setFixedSize(QSize(300,60))
        textEdit.setText("Hello World\nHello")
        layout.addWidget(QLabel('2、显示多行文本')) 
        layout.addWidget(textEdit)   

        textEdit = QTextEdit(self)
        textEdit.setFixedSize(QSize(300,30))
        textEdit.setText("<h1>Hello World</h1>")
        layout.addWidget(QLabel('3、显示html')) 
        layout.addWidget(textEdit)


        widget.setLayout(layout)
        scrollArea.setWidget(widget)
        mainLayout.addWidget(scrollArea)

        self.setLayout(mainLayout)


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