import sys
import os

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QWidget,QSizePolicy
from PyQt6 import  QtGui

class TipLabel(QWidget):
    def __init__(self, showText, tipText, parent=None):
        super().__init__(parent)
        self.label1 = QLabel(showText)
        # 设置size policy为固定大小但可伸缩，即当父控件变大时，控件也会变大
        self.label1.setMaximumWidth(200)
        #self.label1.setStyleSheet("QLabel { background-color: cyan; }")
        self.label2 = QLabel()
        self.label2.setFixedSize(QSize(25, 25))
        image=QtGui.QPixmap("./images/icon_tip.svg")
        
        self.label2.setPixmap(image)
        self.label2.setScaledContents(True)
        self.label2.setToolTip(tipText)
        #self.label1.leaveEvent=self.showToolTip()
        #self.label1.hideEvent=self.hideToolTip()
 
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
 
        self.setLayout(layout)

    def showToolTip(self, event):
        QToolTip.showText(self.mapToGlobal(self.iconLabel.pos()), self.iconLabel.toolTip(), self.iconLabel, self.iconLabel.rect())
 
    def hideToolTip(self, event):
        QToolTip.hideText()

class Demo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        print('Demo init',parent)
        layout = QVBoxLayout(self.parent)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        btn = QPushButton('点我',self)
        btn.setFixedSize(150,30)
        btn.setDefault(True)
        btn.clicked.connect(self.onButtonClicked)
        layout.addWidget(QLabel('1、标准文字按钮及点击事件'))
        layout.addWidget(btn)

        #btn = QPushButton(QIcon(f'{self.parent.getAppDir()}/resources/confirm.png'),'Icon Button',self)  
        btn = QPushButton(parent=self) 
        btn.setIcon(QIcon("./images/icon_add.svg"))   
        btn.setText("增加")  
        btn.setFixedSize(QSize(80, 30))
        btn.clicked.connect(self.onIconButtonClicked)
        layout.addWidget(QLabel('2、按钮加载图标'))
        layout.addWidget(btn)

        btn = QPushButton('Checkable事件按钮',self,checkable=True)
        btn.setFixedSize(150,30)
        btn.clicked.connect(self.onCheckButtonClicked)
        layout.addWidget(QLabel('3、isChecked事件'))
        layout.addWidget(btn)

        btn = QPushButton('重复发送信号按钮',self,autoRepeat=True)
        btn.setFixedSize(150,30)
        btn.clicked.connect(self.onAutoRepeatButtonClicked)
        tip_text='QPushButton的autoRepeat属性用于控制按钮在用户按住鼠标按钮时是否自动重复发送信号。默认情况下，autoRepeat是关闭的。如果你想让按钮在用户按住鼠标时自动重复发送信号，你可以将autoRepeat属性设置为True'
        layout.addWidget(TipLabel('4、autoRepeat属性',tip_text))
        layout.addWidget(btn)


        group = QGroupBox('5、设置按钮可用/不可用状态')
        groupLayout = QHBoxLayout()
        groupLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.btnEnable1 = QPushButton('设置右边按钮不可用',self,checkable=True)
        self.btnEnable1.setFixedSize(150,30)
        self.btnEnable1.clicked.connect(self.onEnableButtonClicked)
        groupLayout.addWidget(self.btnEnable1)

        self.btnEnable2 = QPushButton('按钮可用',self)
        self.btnEnable2.setFixedSize(150,30)
        groupLayout.addWidget(self.btnEnable2)

        groupLayout.addWidget(btn)
        group.setLayout(groupLayout)
        layout.addWidget(group)

        button = QPushButton('菜单按钮', self)
        # 创建弹出菜单和两个动作选项
        menu = QMenu()
        action1 = QAction('选项1', self)
        action1.triggered.connect(self.onOption1Clicked)
        menu.addAction(action1)

        action2 = QAction('选项2', self)
        action2.triggered.connect(self.onOption2Clicked)
        menu.addAction(action2)

        # 将弹出菜单与按钮关联起来，当点击按钮时，会弹出此菜单
        button.setMenu(menu)
        button.setFixedSize(150,30)
        layout.addWidget(QLabel('6、菜单按钮'))
        layout.addWidget(button)

        self.setLayout(layout)

    

    def onButtonClicked(self,event):            
        self.parent.showMessage('Default Button Clicked')
    
    def onIconButtonClicked(self,event):            
        self.parent.showMessage('Icon Button Clicked')

    def onCheckButtonClicked(self,event):
        self.parent.showMessage(f'Checkable Button Clicked,isChecked:{event}')

    def onAutoRepeatButtonClicked(self,event):
        self.parent.showMessage(f'Auto Repeat Button Clicked')

    def onAutoRepeatDelayButtonClicked(self,event):
        self.parent.showMessage(f'Auto Repeat Delay Button Clicked')

    def onAutoRepeatIntervalButtonClicked(self,event):
        self.parent.showMessage(f'Auto Repeat Interval Button Clicked')

    def onEnableButtonClicked(self,event):
        isChecked=event
        if isChecked:
            self.btnEnable2.setText('按钮不可用')
            self.btnEnable2.setEnabled(False)
            self.btnEnable1.setText('设置右边按钮可用')
        else :
            self.btnEnable2.setText('按钮可用')
            self.btnEnable2.setEnabled(True)
            self.btnEnable1.setText('设置右边按钮不可用')
        self.parent.showMessage(f'EnableButton Clicked,isChecked:{event}')

    def onOption1Clicked(self):
        self.parent.showMessage(f'option1_clicked')

    def onOption2Clicked(self):
        self.parent.showMessage(f'option2_clicked')
        

def runDemo(parent):
    print('runDemo',parent)
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