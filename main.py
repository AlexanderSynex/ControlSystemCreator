from PyQt6.QtWidgets import QApplication, QWidget, QTabWidget

from packages import QSystemEditor, QSystemViewer
from packages.QtWidgets.MainWidget import MainWidget
def main():
    app = QApplication([])
    window = MainWidget()
    # window = QSystemViewer()
    window.show()
    
    return app.exec()


if __name__ == '__main__':
    main()
    