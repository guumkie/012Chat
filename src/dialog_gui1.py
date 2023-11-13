# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '012Chat_changename.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from os import environ
from PyQt5 import QtCore, QtGui, QtWidgets

#해상도 설정 start
def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"
#해상도 설정 end

class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        suppress_qt_warnings()
        self.fontDB = QtGui.QFontDatabase()
        self.fontDB.addApplicationFont("../resource/SEBANG Gothic.ttf")
        self.setFont(QtGui.QFont("SEBANG Gothic", 10))
        self.setupUi()
        self.nickname = None

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(750, 264)
        self.setMinimumSize(QtCore.QSize(750, 264))
        self.setMaximumSize(QtCore.QSize(750, 264))
        self.setAutoFillBackground(False)
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Text_title = QtWidgets.QLabel(self)
        self.Text_title.setGeometry(QtCore.QRect(40, 36, 255, 28))
        self.Text_title.setStyleSheet("color: #343A40;")
        self.Text_title.setFont(QtGui.QFont("SEBANG Gothic", 12))
        self.Text_title.setObjectName("Text_title")
        self.Text_Contents = QtWidgets.QLabel(self)
        self.Text_Contents.setGeometry(QtCore.QRect(40, 76, 251, 24))
        self.Text_Contents.setStyleSheet("color: #343A40;")
        self.Text_Contents.setFont(QtGui.QFont("SEBANG Gothic", 9))
        self.Text_Contents.setObjectName("Text_Contents")
        self.Rect_inputBox = QtWidgets.QLabel(self)
        self.Rect_inputBox.setGeometry(QtCore.QRect(40, 104, 670, 44))
        self.Rect_inputBox.setStyleSheet("border-radius: 8px;\n"
"border: 1px solid #ADB5BD;")
        self.Rect_inputBox.setText("")
        self.Rect_inputBox.setObjectName("Rect_inputBox")
        self.Input_text = QtWidgets.QLineEdit(self)
        self.Input_text.setGeometry(QtCore.QRect(56, 117, 638, 17))
        self.Input_text.setStyleSheet("border-style: none;\n"
"color: #ADB5BD;")
        self.Input_text.setText("")
        self.Input_text.setMaxLength(12)
        self.Input_text.setObjectName("Input_text")
        self.Input_text.setFont(QtGui.QFont("SEBANG Gothic", 10))

        self.btn_ok = QtWidgets.QPushButton(self)
        self.btn_ok.setGeometry(QtCore.QRect(530, 184, 180, 44))
        self.btn_ok.setStyleSheet("background-color: #6F3FE2;\n"
"selection-background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"selection-color: #6F3FE2;\n"
"border: 1px solid #6F3FE2;\n"
"border-radius: 8px;\n")
        self.btn_ok.setFont(QtGui.QFont("SEBANG Gothic", 10))
        self.btn_ok.setObjectName("btn_ok")
        self.btn_ok.clicked.connect(self.btnOk_clicked)
        self.btn_no = QtWidgets.QPushButton(self)
        self.btn_no.setGeometry(QtCore.QRect(334, 184, 180, 44))
        self.btn_no.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"selection-background-color: #6F3FE2;\n"
"color: #6F3FE2;\n"
"selection-color: rgb(255, 255, 255);\n"
"border: 1px solid #6F3FE2;\n"
"border-radius: 8px;\n")
        self.btn_no.setObjectName("btn_no")
        self.btn_no.setFont(QtGui.QFont("SEBANG Gothic", 10))
        self.btn_no.clicked.connect(self.btnNo_clicked)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Change Nickname"))
        self.Text_title.setText(_translate("Dialog", "Sure you want to change?"))
        self.Text_Contents.setText(_translate("Dialog", "Write your name (1~12)"))
        self.Input_text.setPlaceholderText(_translate("Dialog", "Nickname"))
        self.btn_no.setText(_translate("Dialog", "No, cancel"))
        self.btn_ok.setText(_translate("Dialog", "Yes, confirm"))

    def btnOk_clicked(self):
        newNick = self.Input_text.text()
        if newNick:
            self.nickname = newNick
            self.accept()

    def btnNo_clicked(self):
        self.reject()

import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
