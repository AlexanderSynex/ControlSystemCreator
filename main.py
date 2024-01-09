from PyQt6.QtWidgets import QApplication, QWidget

from packages import QSystemEditor

def main():
    app = QApplication([])
    
    window = QSystemEditor()
    window.show()
    
    return app.exec()


if __name__ == '__main__':
    main()
    