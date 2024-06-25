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

        lineEdit = QLineEdit("Hello World", self)
        lineEdit.setFixedSize(QSize(300,30))
        layout.addWidget(QLabel('1、显示文本')) 
        layout.addWidget(lineEdit)   

        lineEdit = QLineEdit()
        lineEdit.setText("Hello World")
        lineEdit.setFixedSize(QSize(300,30))
        lineEdit.setReadOnly(True)
        layout.addWidget(QLabel('2、只读')) 
        layout.addWidget(lineEdit)

        lineEdit = QLineEdit('123456')
        lineEdit.setFixedSize(QSize(300,30))
        lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(QLabel('3、显示密码')) 
        layout.addWidget(lineEdit)

        lineEdit = QLineEdit('123')
        lineEdit.setFixedSize(QSize(300,30))
        lineEdit.setValidator(QIntValidator(1,100))
        layout.addWidget(QLabel('4、只能输入数字(1-999)')) 
        layout.addWidget(lineEdit)

        self.lineEdit = QLineEdit('123')
        self.lineEdit.setFixedSize(QSize(300,30))
        layout.addWidget(QLabel('5、全选、复制、剪切、粘贴功能')) 
        #全选按钮
        layoutBtn = QHBoxLayout()
        layoutBtn.setAlignment(Qt.AlignmentFlag.AlignLeft)
        btnSelectAll=QPushButton("全选")
        btnSelectAll.clicked.connect(self.onBtnSelectAllClicked)
        layoutBtn.addWidget(btnSelectAll)
        #剪切按钮
        btnSelectAll=QPushButton("剪切")
        btnSelectAll.clicked.connect(self.onBtnCutClicked)
        layoutBtn.addWidget(btnSelectAll)
        #复制按钮
        btnSelectAll=QPushButton("复制")
        btnSelectAll.clicked.connect(self.onBtnCopyClicked)
        layoutBtn.addWidget(btnSelectAll)
        #粘贴按钮
        btnSelectAll=QPushButton("粘贴")
        btnSelectAll.clicked.connect(self.onBtnPastClicked)
        layoutBtn.addWidget(btnSelectAll)
        layout.addLayout(layoutBtn)
        layout.addWidget(self.lineEdit)


        widget.setLayout(layout)
        scrollArea.setWidget(widget)
        mainLayout.addWidget(scrollArea)

        self.setLayout(mainLayout)

    def onBtnSelectAllClicked(self,event):
        self.lineEdit.selectAll()

    def onBtnCutClicked(self,event):
        self.lineEdit.cut()

    def onBtnCopyClicked(self,event):
        self.lineEdit.copy()

    def onBtnPastClicked(self,event):
        self.lineEdit.paste()


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