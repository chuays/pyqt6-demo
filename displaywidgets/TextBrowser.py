import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QWidget
from PyQt6.QtMultimedia import  QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget

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

        textBrowser = QTextBrowser(self)
        textBrowser.setText("Hello World\nHello World\nHello World")
        textBrowser.setFixedSize(QSize(300,50))
        layout.addWidget(QLabel('1、显示多行文本')) 
        layout.addWidget(textBrowser)   

        textBrowser = QTextBrowser(self)
        textBrowser.setHtml("<h1>Hello, 学习使用TextBrowser！</h1><p>这是一段 <b>粗体</b> 和 <i>斜体</i> 文本.</p><p><a href=\"https://www.baidu.com\">请点击这里</a></p>")
        textBrowser.setOpenExternalLinks(True) # 这行必须加上
        textBrowser.setFixedSize(QSize(600,100))
        layout.addWidget(QLabel('2、显示html')) 
        layout.addWidget(textBrowser) 

        self.textBrowser2 = QTextBrowser(self)
        self.textBrowser2.setHtml("<h1>Hello, 学习使用TextBrowser槽函数！</h1><p><a href=\"https://www.baidu.com\">请点击这里</a></p>")
        self.textBrowser2.setFixedSize(QSize(600,100))
        self.textBrowser2.anchorClicked.connect(self.handleAnchorClicked)
        self.textBrowser2.highlighted.connect(self.handleHighlighted)
        layout.addWidget(QLabel('3、显示html')) 
        layout.addWidget(self.textBrowser2) 

        textBrowser = QTextBrowser(self)
        textBrowser.setSource(QUrl.fromLocalFile('./resources/markdown_sample.md'),
                              QTextDocument.ResourceType.MarkdownResource)
        textBrowser.setFixedSize(QSize(600,100))
        layout.addWidget(QLabel('4、导入markdown文件显示')) 
        layout.addWidget(textBrowser) 


        widget.setLayout(layout)
        scrollArea.setWidget(widget)
        mainLayout.addWidget(scrollArea)

        self.setLayout(mainLayout)

    def handleAnchorClicked(self,url: QUrl):
        print("Anchor clicked:",url.toDisplayString())
        self.parent.showMessage('textBrowser2 handleAnchorClicked url:'+url.toDisplayString())
        QDesktopServices.openUrl(url)

    def handleHighlighted(self):
        print("handleHighlighted")
        self.parent.showMessage('textBrowser2 handleHighlighted')



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