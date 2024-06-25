import sys
from PyQt6.QtWidgets import QApplication, QTextBrowser,QMainWindow,QMenuBar,QMenu,QStatusBar,QMessageBox,QToolBar,QDockWidget,QTextEdit
from PyQt6.QtCore import Qt,QRect,QCoreApplication,QTimer,QMetaObject,QSize
from PyQt6.QtGui import QIcon, QPixmap,QAction
from datetime import datetime

 
class Ui_MainWindow(QMainWindow):
    """主窗体类"""
    def __init__(self):
        """构造函数"""
        super(Ui_MainWindow,self).__init__()        # 调用父类初始化函数，需要调用父类初始化才能正常使用父类定一的变量
        # 其他代码块
        self.setWindowFlag(Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("MyMainWindow")
        MainWindow.resize(800, 600)

        self.setupMenuBar()  
        self.setupCentralWidget()
        self.setupToolBar()
        self.setupDockerWidget()
        self.setupStatusBar()
        print('Ui_MainWindow init finish')
        #用于自动连接信号和槽的方法。它会查找对象的所有属性，
        # 如果属性名称符合特定的命名规则（即以 "on_" 开头），
        # 那么会尝试将该属性自动与相应的信号连接起来。
        QMetaObject.connectSlotsByName(MainWindow)

    def setupCentralWidget(self):

        label=QTextBrowser()
        label.setText('主窗体类是通用的主窗体，包含菜单栏（QMenuBar），工具栏（QToolBars），悬停部件（QDockWidgets）、中央部件（Central Widget）、状态栏（QStatusBar）等基本类型。')
        self.setCentralWidget(label)

    #菜单栏
    def setupMenuBar(self):

        self.menubar = QMenuBar(parent=self)
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QMenu(parent=self.menubar)
        self.menu.setObjectName("menu")
        self.menubar.addMenu(self.menu)
        self.menu_2 = QMenu(parent=self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menubar.addMenu(self.menu_2)

        self.setMenuBar(self.menubar)

        _translate = QCoreApplication.translate
        self.menu.setTitle(_translate("MainWindow", "图书管理"))
        self.menu_2.setTitle(_translate("MainWindow", "设置"))

        #增加子菜单
        self.action = QAction(parent=self)
        icon1 = QIcon()
        icon1.addPixmap(QPixmap("./images/icon_add.svg"), QIcon.Mode.Normal, QIcon.State.Off)
        self.action.setIcon(icon1)
        self.action.setObjectName("action")
        self.action_2 = QAction()
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("./images/icon_info_mgr.svg"), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_2.setIcon(icon2)
        self.action_2.setObjectName("action_2")
        self.action_3 = QAction()
        icon3 = QIcon()
        icon3.addPixmap(QPixmap("./images/icon_toolbar.svg"), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_3.setObjectName("action_3")
        self.action_3.setIcon(icon3)
        self.action_3.setEnabled(False)
        self.action_4 = QAction()
        icon4 = QIcon()
        icon4.addPixmap(QPixmap("./images/icon_quit.svg"), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_4.setIcon(icon4)
        self.action_4.setObjectName("action_4")
        self.action_5 = QAction()
        self.action_5.setObjectName("action_5")
        icon5 = QIcon()
        icon5.addPixmap(QPixmap("./images/icon_about.svg"), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_5.setIcon(icon5)
        self.action_6 = QAction()
        icon6 = QIcon()
        icon6.addPixmap(QPixmap("./images/icon_docker_widget.svg"), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_6.setObjectName("action_6")
        self.action_6.setIcon(icon6)
        self.action_6.setEnabled(False)
 
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu_2.addAction(self.action_3)
        self.menu_2.addAction(self.action_6)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_4)     
        self.menu_2.addAction(self.action_5)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.action.setText(_translate("MainWindow", "图书添加"))
        self.action_2.setText(_translate("MainWindow", "图书信息管理"))
        self.action_3.setText(_translate("MainWindow", "显示工具栏"))
        self.action_4.setText(_translate("MainWindow", "安全退出"))
        self.action_5.setText(_translate("MainWindow", "关于"))
        self.action_6.setText(_translate("MainWindow", "显示悬浮窗"))

        

        #菜单绑定点击事件
        self.menu_2.triggered.connect(self.onMenuClicked)

    def onMenuClicked(self,m):
        if m.text()=="安全退出":
            reply=QMessageBox.question(self,"系统提示",'确认退出吗?',
                                   QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No,
                                   QMessageBox.StandardButton.No)
            if reply==QMessageBox.StandardButton.Yes:
                self.close()
        elif m.text()=="关于":
            QMessageBox.information(None,'关于','主窗体（MainWindow）demo。\n包含菜单栏（QMenuBar），\n工具栏（QToolBars），\n悬停部件（QDockWidgets）、\n中央部件（Central Widget）、\n状态栏（QStatusBar）\n等基本类型')
        elif m.text()=="显示工具栏":
            self.setupToolBar()
            self.action_3.setEnabled(False)
        elif m.text()=="显示悬浮窗":
            self.setupDockerWidget()
            self.action_6.setEnabled(False)

    def setupDockerWidget(self):
        # 创建一个QDockWidget部件
        dock = QDockWidget("Dockable Widget", self)
        dock.setFixedSize(QSize(100,50))

        
        # 创建一个QTextEdit部件并将其添加到QDockWidget中
        editor = QTextEdit()
        dock.setWidget(editor)
        
        # 将QDockWidget添加到QMainWindow中
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock)

        # 连接关闭事件的信号到自定义槽函数
        #dock.topLevelChanged.connect(self.onDockClosed)
        dock.visibilityChanged.connect(self.onDockClosed)

    def onDockClosed(self, visibility):
        # 这个槽函数会在QDockWidget关闭时调用
        print("Dock widget onDockClosed,",visibility)
        if visibility:
            self.action_6.setEnabled(False)
        else:
            self.action_6.setEnabled(True)


    def setupToolBar(self):
        # 创建一个工具栏
        self.toolbar = QToolBar("My Toolbar")

        # 创建一些动作
        newAction = QAction("新建", self)
        newAction.triggered.connect(self.onToolBarNewAction)

        openAction = QAction("打开", self)
        openAction.triggered.connect(self.onToolBarOpenAction)

        savAction = QAction("保存", self)
        savAction.triggered.connect(self.onToolBarSaveAction)

        closeAction = QAction("关闭", self)
        closeAction.triggered.connect(self.onToolBarCloseAction)

        # 将动作添加到工具栏
        self.toolbar.addAction(newAction)
        self.toolbar.addAction(openAction)
        self.toolbar.addAction(savAction)
        self.toolbar.addAction(closeAction)

        # 将工具栏添加到主窗口
        self.addToolBar(self.toolbar)


    def onToolBarNewAction(self):
        QMessageBox.information(None,'工具栏','点击新建')

    def onToolBarOpenAction(self):
        QMessageBox.information(None,'工具栏','点击打开')

    def onToolBarSaveAction(self):
        QMessageBox.information(None,'工具栏','点击保存')
    
    def onToolBarCloseAction(self):
        self.removeToolBar(self.toolbar)
        self.action_3.setEnabled(True)

    #状态栏显示当前时间
    def setupStatusBar(self):
        self.statusbar = self.statusBar()
        self.statusbar.showMessage("时间准备就绪")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # 每秒更新一次

    def update_time(self):
        # 当前日期时间
        now = datetime.now()
        
        # 格式化日期时间
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        time_string = "当前时间: {}".format(formatted_date)
        self.statusbar.showMessage(time_string, 0)

def main():
    app = QApplication(sys.argv)
    main = Ui_MainWindow()
    main.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()