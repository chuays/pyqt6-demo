import sys
from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout,QPushButton,QLineEdit
from PyQt6.QtWidgets import QMessageBox,QFileDialog,QFontDialog,QColorDialog,QInputDialog,QProgressDialog,QErrorMessage
from PyQt6.QtCore import Qt,QCoreApplication
from PyQt6.QtGui import QColor
from forms.NormalDialog import Ui_Dialog


class Demo(QWidget):

    def __init__(self,parent=None):
        super(Demo,self).__init__()

        self.parent=parent
        self.setupUi()

    def setupUi(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        btnNormal = QPushButton('自定义Dialog',self)
        btnNormal.setFixedSize(150,30)
        btnNormal.clicked.connect(self.onBtnNormalClicked)
        layout.addWidget(btnNormal)   

        self.btnMessagebox = QPushButton('messagebox',self)
        self.btnMessagebox.setFixedSize(150,30)
        self.btnMessagebox.clicked.connect(self.onBtnMessageboxClicked)
        layout.addWidget(self.btnMessagebox)   

        self.btnErrorMessage = QPushButton('ErrorMessage',self)
        self.btnErrorMessage.setFixedSize(150,30)
        self.btnErrorMessage.clicked.connect(self.onBtnErrorMessageClicked)
        layout.addWidget(self.btnErrorMessage)   

        self.btnFileDialog = QPushButton('FileDialog',self)
        self.btnFileDialog.setFixedSize(150,30)
        self.btnFileDialog.clicked.connect(self.onBtnFileDialogClicked)
        layout.addWidget(self.btnFileDialog)   

        self.btnFontDialog = QPushButton('FontDialog',self)
        self.btnFontDialog.setFixedSize(150,30)
        self.btnFontDialog.clicked.connect(self.onBtnFontDialogClicked)
        layout.addWidget(self.btnFontDialog) 

        self.btnColorDialog = QPushButton('ColorDialog',self)
        self.btnColorDialog.setFixedSize(150,30)
        self.btnColorDialog.clicked.connect(self.onBtnColorDialogClicked)
        layout.addWidget(self.btnColorDialog)  

        self.btnInputDialog = QPushButton('InputDialog',self)
        self.btnInputDialog.setFixedSize(150,30)
        self.btnInputDialog.clicked.connect(self.onBtnInputDialogClicked)
        layout.addWidget(self.btnInputDialog)  

        self.btnProcessDialog = QPushButton('ProcessDialog',self)
        self.btnProcessDialog.setFixedSize(150,30)
        self.btnProcessDialog.clicked.connect(self.onBtnProcessDialogClicked)
        layout.addWidget(self.btnProcessDialog)  


    def onBtnNormalClicked(self):
        self.dialog = Ui_Dialog()
        self.dialog.show()

    def onBtnMessageboxClicked(self):
        QMessageBox.information(None,'提示','messagebox框')

    def onBtnErrorMessageClicked(self):
        errmsg = QErrorMessage(self)
        errmsg.setWindowTitle('错误提示')
        errmsg.showMessage('错误信息内容')

    def onBtnFileDialogClicked(self): 

        file_name, _ = QFileDialog.getOpenFileName(None, 'Open file', 'c:/')
        print(file_name)
        self.parent.showMessage(f'onBtnFileDialogClicked getOpenFileName:{file_name}')

    def onBtnFontDialogClicked(self): 
        font, ok = QFontDialog.getFont()
        if ok:
            self.parent.showMessage(f'onBtnFontDialogClicked getFont name:{font.family()},bold:{font.bold()},size:{font.pointSize()}')

    def onBtnColorDialogClicked(self):
        # 避免窗口置顶后，Dialog被主窗口覆盖，所以需要传递self
        # 设定默认颜色使用getColor的第一个参数（使用setCurrentColor不生效）
        # "选择颜色" 为Dialog弹窗的标题
        # 设定QColorDialog.ColorDialogOption.ShowAlphaChannel 显示透明度设定
        color = QColorDialog(self).getColor(
                QColor(24, 24, 24, 240), self, "选择颜色", QColorDialog.ColorDialogOption.ShowAlphaChannel)
        if color.isValid():
            print(color.name())
            print(str(color.alpha()))
            self.parent.showMessage(f'onBtnColorDialogClicked name:{color.name()} alpha:{str(color.alpha())}')

    def onBtnInputDialogClicked(self): 
        text, okPressed = QInputDialog.getText(self, "Get text","Your name:", QLineEdit.EchoMode.Normal, "aaa")
        if okPressed and text != '':
            print(text)

            self.parent.showMessage(f'onBtnInputDialogClicked getText:{text}')

    def onBtnProcessDialogClicked(self):
        """进度对话框"""
        elapsed = 200000
        # QProgressDialog组件定义
        self.progressDialog = QProgressDialog('下载进度', '取消', 0, elapsed, self)
        # QProgressDialog关联信号
        self.progressDialog.canceled.connect(self.on_progressDialog_canceled)
        # QProgressDialog组件设置
        self.progressDialog.setWindowTitle('QProgressDialog组件示例')
        self.progressDialog.setWindowModality(Qt.WindowModality.WindowModal)
        self.progressDialog.show()
        for val in range(elapsed):
            self.progressDialog.setValue(val)       # 设置当前的进度值
            QCoreApplication.processEvents()        # 实时刷新页面
            if self.progressDialog.wasCanceled():   # 判断是否点了取消按钮
                break
        self.progressDialog.setValue(elapsed)

    def on_progressDialog_canceled(self):
        """槽函数"""
        print("progressDialog进度对话框被取消啦！")
        self.parent.showMessage(f'progressDialog进度对话框被取消啦')


def runDemo(parent):
    print('runDemo',parent)
    wigdet =  Demo(parent)
    
    return wigdet

def main():
    app = QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()