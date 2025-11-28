# GUI = Graphical User Interface
# PyQt5 introduction
# Pop-up window that we usually saw maybe online Ads

import sys # System specific parameters functions
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Cool PyQt5 GUI")
        self.setGeometry(400, 300, 500, 500) # (x, y, width, height)
        self.setWindowIcon(QIcon("xyz.jpg")) # Add picture to be an icon

def main():
    app = QApplication(sys.argv) # Access the modules arguments
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) # Execute method

if __name__ == "__main__":
    main()