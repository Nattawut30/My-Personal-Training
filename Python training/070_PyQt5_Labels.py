# PyQt5 QLabels

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        # Customization
        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: yellow;"
                            "background-color: blue;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")

        #label.setAlignment(Qt.AlignTop) #VERTICALLY TOP
        #label.setAlignment(Qt.AlignBottom) # VERTICALLY BOTTOM
        #label.setAlignment(Qt.AlignHCenter)  # VERTICALLY CENTER

        #label.setAlignment(Qt.AlignRight) # HORIZONTALLY RIGHT
        #label.setAlignment(Qt.AlignCenter) # HORIZONTALLY CENTER
        #label.setAlignment(Qt.AlignLeft) # HORIZONTALLY LEFT

        # label.setAlignment(Qt.AlignCenter | Qt.AlignTop) # CENTER & TOP
        # label.setAlignment(Qt.AlignCenter | Qt.AlignBottom) # CENTER & BOTTOM
        # label.setAlignment(Qt.AlignCenter | Qt.AlignCenter) # CENTER & CENTER
        label.setAlignment(Qt.AlignCenter) # CENTER & CENTER

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
