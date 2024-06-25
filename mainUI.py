import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QStandardItemModel,QStandardItem,QPainter,QColor,QIcon
from PyQt6.QtCore import *
import os
from button import PushButton,CheckBox,RadioButton
from forms import Dialog
from layouts import HBoxLayout,VBoxLayout,GridLayout
from displaywidgets import Label,TextBrowser
from inputwidgets import LineEdit,TextEdit,PlainTextEdit,ComboBox
from containers import GroupBox,ScrollArea
from forms import Application,MainWindow
from forms.MainWindow import Ui_MainWindow
from forms.Widget import Ui_Form
from forms.NormalDialog import Ui_Dialog
import datetime


currentDir = os.path.split(os.path.abspath(sys.argv[0]))[0]
currentDirButton=currentDir+'/button'

allFileDirs=['forms','button','layouts','containers','inputwidgets','displaywidgets']

class CustomTreeView(QTreeView):
        def __init__(self, parent=None):
            super().__init__(parent)

        def paintEvent(self, event):
            painter = QPainter(self.viewport())

            for index in self.selectedIndexes():
                rect = self.visualRect(index)
                painter.fillRect(rect, QColor("lightblue"))

            super().paintEvent(event)

        def data(self, index: QModelIndex, role: int):
            if not index.isValid():
                return None
            print('CustomTreeView data',role)
            if role == Qt.ItemDataRole.DecorationRole:
                file_info = self.model().fileInfo(index)
                if file_info.isDir():
                    return QIcon("./images/btn_icon.svg")
                else:
                    return QIcon("./images/btn_icon.svg")

            return super().data(index, role)

class MainWindow(QMainWindow):

    dataModel = QStandardItemModel()
    def __init__(self):
        super(MainWindow,self).__init__()

        self.treeData = [('forms',['Application', 'MainWindow', 'Widget', 'Dialog',]),
                    ('button',['PushButton', 'CheckBox', 'RadioButton']),
                    ('layouts',['HBoxLayout', 'VBoxLayout', 'GridLayout']),
                    ('containers',['GroupBox','ScrollArea']),
                    ('inputwidgets',['ComboBox','LineEdit','TextEdit','PlainTextEdit']),
                    ('displaywidgets',['Label','TextBrowser'])]
        self.title='PyQt6 Demo'
       
        self.setWindowTitle('PyQt6 Demo')
        

        self.currentSelectedMenu=None
        self.currentSelectedMenuParent=None

        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.setChildrenCollapsible(False)

        #左侧布局
        leftWidget = QWidget()
        leftLayout = QVBoxLayout()
        #左侧树
        self.treeView = CustomTreeView()
        self.treeView.setStyleSheet('background-color: #ffffff;')
        self.treeView.setEditTriggers(QTreeView.EditTrigger.NoEditTriggers)
        self.treeView.clicked.connect(self.onTreeClicked)
        self.treeView.setModel(self.dataModel)    
        self.dataModel.setHorizontalHeaderLabels([self.title])        
        self.searchTxt = QLineEdit()
        self.searchTxt.textChanged.connect(self.initTree)        
        
        leftLayout.addWidget(QLabel('Filter Demos:'))        
        leftLayout.addWidget(self.searchTxt)
        leftLayout.addWidget(self.treeView)
        leftWidget.setLayout(leftLayout)

        #右上代码及展示
        self.splitterRightTop = QSplitter(Qt.Orientation.Horizontal)
        self.splitterRightTop.setChildrenCollapsible(False)      
        self.splitterRightTop.setStretchFactor(0,8)
        self.splitterRightTop.setStretchFactor(1,2)
        # 设置父控件的最大宽度
        self.splitterRightTop.setMaximumWidth(400)
        self.codePage = None
        self.demoPage = None
        
        rightPageWidget = QWidget()
        self.btnStatusShowCode= False
        #右上左部分是两个按钮+demo页面
        rightTopButtonLayout = QHBoxLayout()
        self.btnShowIntroduce= QPushButton("隐藏介绍视图")
        self.btnShowIntroduce.clicked.connect(self.showOrHideIntroduceView)
        self.btnShowCode= QPushButton("显示代码")
        self.btnShowCode.clicked.connect(self.showOrHideCodeView)
        self.btnShowLog= QPushButton("隐藏日志")
        self.btnShowLog.clicked.connect(self.showOrHideLogView)
        self.btnOpenForm= QPushButton("打开新窗口")
        self.btnOpenForm.clicked.connect(self.btnOnclickedOpenForm)
        rightTopButtonLayout.addWidget(self.btnShowIntroduce)
        rightTopButtonLayout.addWidget(self.btnShowCode)
        rightTopButtonLayout.addWidget(self.btnShowLog)
        rightTopButtonLayout.addWidget(self.btnOpenForm)

        #右上左部分介绍界面
        self.rightTopIntroduce = QGroupBox()
        self.rightTopIntroduce.setTitle("简介")
        self.introWidget = QTextBrowser()
        self.introWidget.setText("暂未添加")
        groupLayout = QVBoxLayout()
        groupLayout.addWidget(self.introWidget)
        self.rightTopIntroduce.setLayout(groupLayout)

        #右上左部分demo界面
        self.rightPageLayout = QVBoxLayout()
        
        self.rightPageLayout.addLayout(rightTopButtonLayout)
        self.rightPageLayout.addWidget(self.rightTopIntroduce)
        self.rightPageLayout.addWidget(self.demoPage)
        rightPageWidget.setLayout(self.rightPageLayout)
        #右上右部分是代码界面
        self.rightCodeWidget = QWidget()
        self.codePage = QTextEdit()#CodeEditor()   
        rightCodeLayout = QVBoxLayout()
        rightCodeLayout.addWidget(self.codePage)
        self.rightCodeWidget.setLayout(rightCodeLayout)
        self.rightCodeWidget.hide()

        self.splitterRightTop.addWidget(rightPageWidget)
        self.splitterRightTop.addWidget(self.rightCodeWidget)
        
    
        #右下日志消息
        self.rightBottomWidget = QWidget()        
        rightBottomLayout = QVBoxLayout()        
        self.messageTxt = QTextEdit()
        self.messageTxt.setStyleSheet('background-color:#ffffff;')
        self.messageTxt.setReadOnly(True)
        self.messageTxt.setMaximumHeight(50)
        rightBottomLayout.addWidget(QLabel("Demo Log Message:"))
        rightBottomLayout.addWidget(self.messageTxt)
        self.rightBottomWidget.setLayout(rightBottomLayout)
        #self.rightBottomWidget.hide()

        splitterRight = QSplitter(Qt.Orientation.Vertical)
        splitterRight.setChildrenCollapsible(False)
        splitterRight.addWidget(self.splitterRightTop)
        splitterRight.addWidget(self.rightBottomWidget)
        splitterRight.setStretchFactor(0,8)
        splitterRight.setStretchFactor(1,2)

        splitter.addWidget(leftWidget)
        splitter.addWidget(splitterRight)
        splitter.setChildrenCollapsible(False)
        splitter.setStretchFactor(0,2)
        splitter.setStretchFactor(1,8)

        self.setCentralWidget(splitter)

        self.initTree()

        self.loadDemo('forms','MainWindow')

    def loadIntroText(self,demoName):
        fileName = f'{currentDir}/intro/{demoName}.txt'  
        self.showMessage(f'loadIntroText {fileName}')      
        if os.path.exists(fileName) == False:   
            self.introWidget.setText('暂无介绍内容')         
            return        
        self.introWidget.setText( open(fileName,'r',encoding='utf8').read())
        self.introWidget.setFixedHeight(int(self.introWidget.document().size().height()))
        self.introWidget.resize(self.introWidget.size())
        self.rightTopIntroduce.setFixedHeight(self.introWidget.height()+30)
        self.rightTopIntroduce.resize(self.rightTopIntroduce.size())

    def onTreeClicked(self,index):
        '''树点击事件，加载代码及示例'''
        currentItem = self.dataModel.itemFromIndex(index)  
        parentMenuName=None
        if  currentItem.parent():
            parentMenuName=currentItem.parent().text()  
        if currentItem.hasChildren() == False:
            name = str(currentItem.text())
            self.showMessage(f'clicked {name}')
            self.loadDemo(parentMenuName,name)

            self.currentSelectedMenu=name
            self.currentSelectedMenuParent=parentMenuName
            if name =='MainWindow' or name=='Widget' or name=='Dialog' :
                self.btnOpenForm.setEnabled(True)
            else:
                self.btnOpenForm.setEnabled(False)

    def showOrHideCodeView(self):
        if self.btnStatusShowCode:
            self.btnShowCode.setText("显示代码")
            self.btnStatusShowCode = False
            self.rightCodeWidget.hide()
        else :
            self.btnShowCode.setText("隐藏代码")
            self.btnStatusShowCode = True
        
            self.rightCodeWidget.show()

    def showOrHideIntroduceView(self):

        msgLogBtn=self.btnShowIntroduce.text()

        if msgLogBtn=='显示介绍视图':
            self.btnShowIntroduce.setText("隐藏介绍视图")
            self.rightTopIntroduce.show()
        else :
            self.btnShowIntroduce.setText("显示介绍视图")       
            self.rightTopIntroduce.hide()


    def showOrHideLogView(self):

        msgLogBtn=self.btnShowLog.text()

        if msgLogBtn=='显示日志':
            self.btnShowLog.setText("隐藏日志")
            self.rightBottomWidget.show()
        else :
            self.btnShowLog.setText("显示日志")       
            self.rightBottomWidget.hide()

    def btnOnclickedOpenForm(self):
        print('btnOnclickedOpenForm',self.currentSelectedMenu)
        if self.currentSelectedMenu=='Widget':           
            self.uiForm=Ui_Form()
            self.uiForm.show()
        elif self.currentSelectedMenu=='MainWindow':
            self.mainWindow=Ui_MainWindow()
            self.mainWindow.show()
        elif self.currentSelectedMenu=='Dialog':
            self.uiDialog=Ui_Dialog()
            self.uiDialog.show()

    def initTree(self):    
        '''初始化树'''    
        self.dataModel.removeRows(0,self.dataModel.rowCount())
        root = self.dataModel.invisibleRootItem()        
        keyword = str(self.searchTxt.text())
        
        for category, items in self.treeData:
            if keyword:
                items = [item for item in items if keyword.lower() in item.lower()]
            if items:
                categoryItem = QStandardItem(category)
                # 在顶级项左侧添加图标
                categoryItem.setIcon(QIcon('./images/btn_icon.svg')) 
                root.appendRow(categoryItem)
                for child in items:
                    childItem=QStandardItem(child)
                    icon = self.getMenuIcon(child)
                    if icon is not None:
                        childItem.setIcon(icon) 
                    categoryItem.appendRow(childItem)
        self.treeView.expandAll()

    def getMenuIcon(self,menuName):
        filePath='./images/'+menuName+'_icon.svg'
        icon = None
        if os.path.exists(filePath):
            icon = QIcon(filePath)
        return icon

    def loadDemo(self,fileDir,demoName):
        self.loadIntroText(demoName)
        '''加载示例及代码'''     
        self.codePage.setText('')
        #self.rightPageLayout.removeWidget(self.rightPageLayout.widget())
        if self.rightPageLayout.count() > 2:
            widget=self.rightPageLayout.itemAt(2).widget()
            self.rightPageLayout.removeItem(self.rightPageLayout.itemAt(2))
            widget.setParent(None)
        if fileDir is None:
            for dir in allFileDirs:
                fileName = f'{currentDir}/{dir}/{demoName}.py'     
                if os.path.exists(fileName):  
                    fileDir=dir
                    break
        if fileDir is None:   
            print("loadDemo fileDir is none")      
            return    
            
        fileName = f'{currentDir}/{fileDir}/{demoName}.py'    
        print("loadDemo fileName:",fileName)    
        if os.path.exists(fileName) == False:            
            return        
        self.showMessage(f'Loading demo code {demoName}.py...')
        self.codePage.setText( open(fileName,'r',encoding='utf8').read())
        #根据点击菜单显示不同的布局
        if demoName == 'PushButton':
            self.rightPageLayout.addWidget(PushButton.runDemo(self) )
        elif demoName == 'CheckBox':
            self.rightPageLayout.addWidget(CheckBox.runDemo(self) )
        elif demoName == 'RadioButton':
            self.rightPageLayout.addWidget(RadioButton.runDemo(self) )
        elif demoName == 'Dialog':
            self.rightPageLayout.addWidget(Dialog.runDemo(self) )
        elif demoName == 'HBoxLayout':
            self.rightPageLayout.addWidget(HBoxLayout.runDemo(self) )
        elif demoName == 'VBoxLayout':
            self.rightPageLayout.addWidget(VBoxLayout.runDemo(self) )
        elif demoName == 'GridLayout':
            self.rightPageLayout.addWidget(GridLayout.runDemo(self) )
        elif demoName == 'Label':
            self.rightPageLayout.addWidget(Label.runDemo(self) )
        elif demoName == 'TextBrowser':
            self.rightPageLayout.addWidget(TextBrowser.runDemo(self) )
        elif demoName == 'LineEdit':
            self.rightPageLayout.addWidget(LineEdit.runDemo(self) )
        elif demoName == 'TextEdit':
            self.rightPageLayout.addWidget(TextEdit.runDemo(self) )
        elif demoName == 'PlainTextEdit':
            self.rightPageLayout.addWidget(PlainTextEdit.runDemo(self) )
        elif demoName == 'ComboBox':
            self.rightPageLayout.addWidget(ComboBox.runDemo(self) )
        elif demoName == 'GroupBox':
            self.rightPageLayout.addWidget(GroupBox.runDemo(self) )
        elif demoName == 'ScrollArea':
            self.rightPageLayout.addWidget(ScrollArea.runDemo(self) )
        

    def showMessage(self,msg):
        '''显示日志'''
        self.messageTxt.append(f'{datetime.datetime.now().strftime("%H:%M:%S.%f")} {msg}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()        
    main.showMaximized()
    sys.exit(app.exec())