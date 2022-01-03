import sys
import os
from PyQt5.QtCore import*
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
  
        #Resize Window
        self.resize(650, 400)
        
        self.layout = QGridLayout()
        
        #App name label
        app_name = QLabel('Form Autofill')
        app_name.setFixedSize(291, 81)
        app_name.setAlignment(Qt.AlignCenter)
        app_name.setStyleSheet(
                    "color: rgb(255, 255, 225);"
                    "font: 36pt \"Bahnschrift SemiLight\";"
                    )
        self.layout.addWidget(app_name, 0, 1)


        #Username input
        label_name = QLabel('<font size="5"> Username </font>')
        label_name.setStyleSheet(
                "font: 75 14pt \"MS Shell Dlg 2\";"
                "color: rgb(255, 255, 255);"
                )

        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setStyleSheet(
                "background-color: rgb(255, 255, 255);"
                "border: none"
                )
        self.lineEdit_username.setPlaceholderText('Please enter your username')
        label_name.setGeometry(QRect(110, 190, 51, 31))
        self.lineEdit_username.setFixedHeight(31)
        self.layout.addWidget(label_name, 1, 0)
        self.layout.addWidget(self.lineEdit_username, 1, 1)
        
        #Password input
        label_password = QLabel('<font size="5"> Password </font>')
        label_password.setStyleSheet(
                    "font: 75 14pt \"MS Shell Dlg 2\";\n"
                    "color: rgb(255, 255, 255);"
                    ) 
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Please enter your password')
        self.lineEdit_password.setStyleSheet(
                    "background-color: rgb(255, 255, 255);"
                    "border: none"
                    )
        self.layout.addWidget(label_password, 2, 0)
        self.layout.addWidget(self.lineEdit_password, 2, 1)
        label_password.setGeometry(QRect(80, 250, 81, 31))
        self.lineEdit_password.setFixedHeight(31)
        
        #Login button
        button_login = QPushButton('Login')
        button_login.clicked.connect(self.check_password)
        self.layout.addWidget(button_login, 3, 1)
        button_login.setFixedSize(111, 41)
        #button_login.setGeometry(QRect(250, 300, 111, 41))
        button_login.setStyleSheet(
                    "font: 75 14pt \"MS Shell Dlg 2\";\n"
                    "background-color: rgb(255, 255, 255);\n"
                    "color: rgb(255, 170, 0);"
                    )

        self.setLayout(self.layout)

    def check_password(self):
        msg = QMessageBox()

        if self.lineEdit_username.text() == 'login' and self.lineEdit_password.text() == '1505':
            msg.setText('Success')
            msg.exec_() 
            app.quit()
        else:
            msg.setText('Incorrect Password')
            msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    form = LoginForm()
    form.setStyleSheet("background-color: rgb(255, 170, 0);")
    form.setFixedSize(650, 400)
    form.show()


    sys.exit(app.exec_())