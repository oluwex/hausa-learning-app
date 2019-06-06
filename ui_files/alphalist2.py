# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Habeeb\Documents\Pycharm Projects\Hausa project\ui_files\alphalist2.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(689, 588)
        Dialog.setStyleSheet("QLabel{\n"
"font: 35px Tempus Sans ITC;\n"
"color: red;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c);\n"
"border: 2px solid gray;\n"
"border-radius: 15px;\n"
"font-size: 30px;\n"
"font-family: Tempus Sans ITC;\n"
"color: white\n"
"}\n"
"\n"
"#btn_close{\n"
"font-size: 24px;\n"
"}")
        self.btn_close = QtWidgets.QPushButton(Dialog)
        self.btn_close.setGeometry(QtCore.QRect(284, 540, 89, 25))
        self.btn_close.setMinimumSize(QtCore.QSize(89, 25))
        self.btn_close.setMaximumSize(QtCore.QSize(89, 25))
        self.btn_close.setObjectName("btn_close")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(54, 80, 591, 441))
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 589, 439))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 10, 561, 61))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.btn_close.clicked.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_close.setText(_translate("Dialog", "Close"))
        self.label.setText(_translate("Dialog", "Select a letter to view"))

