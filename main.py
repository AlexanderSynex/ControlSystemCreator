import sys
from PyQt6.QtWidgets import QApplication, QWidget, QTabWidget

from packages.QtWidgets.MainWindow import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    return app.exec()


if __name__ == '__main__':
    main()
    