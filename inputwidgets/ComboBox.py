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

        self.combobox = QComboBox()
        self.combobox.setMaximumWidth(300)
        self.combobox.addItem("选项1")
        self.combobox.addItem("选项2")
        self.combobox.addItem("选项3")
        self.combobox.currentIndexChanged.connect(self.onComboboxChanged)
        self.displayLabel= QLabel("选择结果："+self.combobox.currentText())
        layout.addWidget(self.displayLabel)
        layout.addWidget(self.combobox)   

        self.setLayout(layout)

    def onComboboxChanged(self,index):
        print(self.combobox.currentText())
        self.displayLabel.setText("选择结果："+self.combobox.currentText())


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