from PyQt6.QtWidgets import QApplication, QWidget

from packages import QSystemEditor, QSystemViewer

def main():
    app = QApplication([])
    
    window = QSystemViewer()
    window.show()
    
    return app.exec()


if __name__ == '__main__':
    main()
    