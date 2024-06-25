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

        label = QLabel("Hello World", self)
        label.setStyleSheet("background-color:gray")
        #label.resize(150, 150)
        label.setFixedSize(QSize(300,50))
        layout.addWidget(QLabel('1、普通label显示文本')) 
        layout.addWidget(label)   

        label = QLabel("Hello World", self)
        label.setStyleSheet("background-color:gray")
        label.setFixedSize(QSize(300,50))
        label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)  # 垂直居中右对齐
        layout.addWidget(QLabel('2、对齐方式(横向居中+垂直上对齐)')) 
        layout.addWidget(label)

        label = QLabel("Hello World！！Hello World！！Hello World！！Hello World！！", self)
        label.setStyleSheet("background-color:gray")
        label.setFixedSize(QSize(300,50))
        label.setIndent(20) # 缩进（单边）
        #label.setMargin(20)  # 边距（两边）
        layout.addWidget(QLabel('3、缩进和边距(单边/双边)')) 
        layout.addWidget(label)

        label = QLabel("Hello World！！Hello World！！Hello World！！Hello World！！", self)
        label.setStyleSheet("background-color:gray")
        label.setFixedSize(QSize(300,50))
        label.setWordWrap(True)
        layout.addWidget(QLabel('4、文本换行')) 
        layout.addWidget(label)

        label = QLabel("<h1>Hello World</h1>", self)
        label.setStyleSheet("background-color:gray")
        label.setFixedSize(QSize(300,50))
        #label.setTextFormat(Qt.TextFormat.PlainText)  # 展示普通文本（比如富文本“<h1>xxx<h1/>”全部展示出来）
        label.setTextFormat(Qt.TextFormat.RichText) 
        layout.addWidget(QLabel('5、文本格式(支持RichText/PlainText/Markdown)')) 
        layout.addWidget(label)

        label = QLabel(parent=self)
        label.setFixedSize(QSize(50,50))
        label.setPixmap(QPixmap("./images/icon_add.svg"))
        label.setScaledContents(True)  # 图片缩放
        layout.addWidget(QLabel('6、显示图片')) 
        layout.addWidget(label)

        label = QLabel(parent=self)
        label.setFixedSize(QSize(50,50))
        movie = QMovie("./images/gif_demo.gif")
        label.setMovie(movie)
        label.setScaledContents(True)
        layout.addWidget(QLabel('7、显示GIF图')) 
        layout.addWidget(label)
        movie.start()

        label = QLabel("<a href='https://www.baidu.com/'>百度<a/>", self)
        label.setStyleSheet("background-color:gray")
        label.setFixedSize(QSize(300,50))
        label.setOpenExternalLinks(True)
        layout.addWidget(QLabel('8、外部链接')) 
        layout.addWidget(label)


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