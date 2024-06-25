import sys
from PyQt6.QtWidgets import QApplication, QLabel
      

def main():
    app = QApplication(sys.argv)
    # 创建一个QLabel实例
    label = QLabel("hello world")      
    label.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()