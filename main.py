from PyQt6.QtWidgets import QApplication, QWidget, QTabWidget

from packages.QtWidgets.MainWidget import MainWidget

def main():
    app = QApplication([])
    window = MainWidget()
    window.show()
    
    return app.exec()


if __name__ == '__main__':
    main()
    