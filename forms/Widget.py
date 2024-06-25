import sys
from PyQt6.QtWidgets import QApplication, QLabel,QWidget
from PyQt6.QtGui import QIcon


class Ui_Form(QWidget):

    def __init__(self):
        super(Ui_Form,self).__init__()
        self.setupUi(self)


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 200)

        self.setWindowIcon(QIcon('./images/icon_app.svg'))
        self.setWindowTitle('widget demo')

        # 创建一个QLabel实例
        label = QLabel("hello world",parent=Form)        

def main():
    app = QApplication(sys.argv)
    form=Ui_Form()
    form.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()