import sys
from PyQt6.QtWidgets import QApplication, QLabel,QDialog


class Ui_Dialog(QDialog):

    def __init__(self):
        super(Ui_Dialog,self).__init__()
        self.setupUi()


    def setupUi(self):
        self.setWindowTitle("dialog demo")
        self.resize(300, 200)
        QLabel('hello,word',parent=self)

def main():
    app = QApplication(sys.argv)
    form=Ui_Dialog()
    form.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()