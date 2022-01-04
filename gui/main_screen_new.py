import sys
import os
from PyQt5.QtCore import*
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        #Main window settings
        self.setWindowTitle('Form Autofill')
        self.resize(850,600)
        #self.setWindowFlags(Qt.FramelessWindowHint)
        #self.setAttribute(Qt.WA_TranslucentBackground)

        #container
        self.container = QFrame()
        self.container.setStyleSheet("background-color: rgb(255, 225, 225);")
        self.layout = QVBoxLayout()

        #central widget
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        #Start button
        button_start = QPushButton('Start')
        button_start.setMinimumSize(150, 150)
        button_start.setStyleSheet("QPushButton {\n"
                        "    font: 26pt \"MS Shell Dlg 2\";\n"
                        "    color: rgb(253, 253, 253);\n"
                        "    border: 2px solid #555;\n"
                        "    border-radius: 75px;\n"
                        "    border-style: none;\n"
                        "    background: qradialgradient(\n"
                        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                        "        radius: 1.35, stop: 0 #fff, stop: 1 #e16500\n"
                        "        );\n"
                        "    padding: 5px;\n"
                        "    }\n"
                        "\n"
                        "QPushButton:hover {\n"
                        "    background: qradialgradient(\n"
                        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                        "        radius: 1.35, stop: 0 #fff, stop: 1 #fa7e00\n"
                        "        );\n"
                        "    }\n"
                        "\n"
                        "QPushButton:pressed {\n"
                        "    border-style: inset;\n"
                        "    background: qradialgradient(\n"
                        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                        "        radius: 1.35, stop: 0 #fff, stop: 1 #af1919\n"
                        "        );\n"
                        "    }")
        
        self.layout.addWidget(button_start, Qt.AlignHCenter, Qt.AlignHCenter)

        #create another layout for forms
        form_layout = QFormLayout()
        form_layout.setGeometry(QRect(130, 120, 600, 400))
        form_layout.setContentsMargins(0, 0, 0, 0)







        #App name label
        # self.app_name_label = QLabel('Form Autofill')
        # self.app_name_label.setMinimumSize(291, 81)
        # self.app_name_label.setStyleSheet(
        #     "color: rgb(255, 255, 255);\n"
        #     "font: 36pt \"Bahnschrift SemiLight\";\n"
        #     )
        # form_layout.addWidget(self.app_name_label)


        self.show()



if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())