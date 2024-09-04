from PySide6.QtWidgets import QApplication
import os
import sys
import MainWindow

def main():
    app = QApplication()
    win = MainWindow.MainWindow()
    win.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()