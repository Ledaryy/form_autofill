# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import os
from PyQt5.QtCore import*
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class Ui_Dialog(QDialog):
    def __init__(self):
        super().__init__()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(850, 600)
        Dialog.setMinimumSize(QSize(850, 600))
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.laptop_box_size = QRadioButton(Dialog)
        self.laptop_box_size.setGeometry(QRect(710, 150, 82, 17))
        self.laptop_box_size.setObjectName("laptop_box_size")
        self.Monitor = QRadioButton(Dialog)
        self.Monitor.setGeometry(QRect(710, 180, 82, 17))
        self.Monitor.setObjectName("Monitor")
        self.pack_type_label = QLabel(Dialog)
        self.pack_type_label.setGeometry(QRect(710, 120, 81, 16))
        self.pack_type_label.setObjectName("pack_type_label")
        self.app_name_label = QLabel(Dialog)
        self.app_name_label.setGeometry(QRect(250, 10, 291, 81))
        self.app_name_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(168, 168, 168);\n"
"font: 36pt \"Bahnschrift SemiLight\";\n"
"")
        self.app_name_label.setObjectName("app_name_label")
        self.start_button = QPushButton(Dialog)
        self.start_button.setGeometry(QRect(300, 260, 150, 150))
        self.start_button.setMaximumSize(QSize(150, 150))
        self.start_button.setStyleSheet("QPushButton {\n"
"    font: 26pt \"MS Shell Dlg 2\";\n"
"    color: rgb(253, 253, 253);\n"
"    border: 2px solid #555;\n"
"    border-radius: 75px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bdb\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.start_button.setAutoDefault(True)
        self.start_button.setDefault(False)
        self.start_button.setObjectName("start_button")
        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QRect(80, 280, 181, 241))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QRect(150, 200, 631, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.open_file_button = QPushButton(self.verticalLayoutWidget)
        self.open_file_button.setObjectName("open_file_button")
        self.verticalLayout.addWidget(self.open_file_button)
        self.file_name = QFrame(self.verticalLayoutWidget)
        self.file_name.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.file_name.setFrameShape(QFrame.StyledPanel)
        self.file_name.setFrameShadow(QFrame.Raised)
        self.file_name.setObjectName("file_name")
        self.verticalLayout.addWidget(self.file_name)
        self.create_template_button = QPushButton(self.verticalLayoutWidget)
        self.create_template_button.setObjectName("create_template_button")
        self.verticalLayout.addWidget(self.create_template_button)

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.laptop_box_size.setText(_translate("Dialog", "Laptop"))
        self.Monitor.setText(_translate("Dialog", "Monitor"))
        self.pack_type_label.setText(_translate("Dialog", "Packaging type"))
        self.app_name_label.setText(_translate("Dialog", "Form Autofill"))
        self.start_button.setText(_translate("Dialog", "START"))
        self.open_file_button.setText(_translate("Dialog", "Open File"))
        self.create_template_button.setText(_translate("Dialog", "Create Template"))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    form = Ui_Dialog()
    form.show()


    sys.exit(app.exec_())