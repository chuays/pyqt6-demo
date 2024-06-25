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
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        cb = QCheckBox('CheckBox',self)        
        cb.clicked.connect(self.onClicked)
        layout.addWidget(QLabel('1、标准checkbox'))
        layout.addWidget(cb)
        #####
        cb = QCheckBox('CheckBox',self)        
        # 设置样式表来调整图标和文字之间的距离,文字大小
        cb.setStyleSheet("QCheckBox{spacing: 50px;font: 30px;}")
        layout.addWidget(QLabel('2、调整图标和文字之间的距离，文字大小'))
        layout.addWidget(cb)
        #####
        cb = QCheckBox('CheckBox',self)        
        cb.setIcon(QIcon('./images/icon_add.svg'))
        layout.addWidget(QLabel('3、文字前面增加图标'))
        layout.addWidget(cb)
        #2、自定义选择框
        cb = QCheckBox('CustomCheckBox',self)        
        # 设置QSS样式
        cb.setStyleSheet("QCheckBox::indicator {\
                width: 20px;\
                height: 20px;\
            }\
            QCheckBox::indicator:checked {\
                image: url('./images/icon_checkbox_selected.svg');\
            }\
            QCheckBox::indicator:unchecked {\
                image: url(./images/icon_checkbox_normal.svg');\
            }\
        ")
        cb.setChecked(True)
        layout.addWidget(QLabel('4、checkbox更换图标'))
        layout.addWidget(cb)

        groupBox = QGroupBox('5、分组CheckBoxes')        
        self.groupExclusive = QButtonGroup()
        self.groupExclusive.setExclusive(False)        
        groupLayout = QVBoxLayout()

        cb = QCheckBox('CheckBox1',self,objectName='CheckBox1')        
        #cb.clicked.connect(self.OnGroupClicked)
        groupLayout.addWidget(cb)
        self.groupExclusive.addButton(cb)

        cb = QCheckBox('CheckBox2',self,objectName='CheckBox2')        
        #cb.clicked.connect(self.OnGroupClicked)
        groupLayout.addWidget(cb)
        self.groupExclusive.addButton(cb)

        cb = QCheckBox('CheckBox3',self,objectName='CheckBox3')        
        #cb.clicked.connect(self.OnGroupClicked)
        groupLayout.addWidget(cb)
        self.groupExclusive.addButton(cb)
        self.groupExclusive.buttonClicked.connect(self.onGroupClicked)

        groupBox.setLayout(groupLayout)
        layout.addWidget(groupBox)        

        self.setLayout(layout)

    def onClicked(self,event):            
        self.parent.showMessage(f'CheckBox Clicked,isChecked:{event}')

    def onGroupClicked(self,event):
        btn = self.groupExclusive.checkedButton()
        if btn :
            self.parent.showMessage(f'Exclusive {btn.text()} Clicked,isChecked:{btn.isChecked()}')
        else :
            self.parent.showMessage('QButtonGroup No checkbox checked!')

    
        

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