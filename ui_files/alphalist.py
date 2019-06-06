# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Habeeb\Documents\Pycharm Projects\Hausa project\ui_files\alphalist.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_alphaPg(object):
    def setupUi(self, alphaPg):
        alphaPg.setObjectName("alphaPg")
        alphaPg.resize(689, 591)
        alphaPg.setStyleSheet("QLabel{\n"
"font: 35px Tempus Sans ITC;\n"
"color: red;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c);\n"
"border: 2px solid gray;\n"
"border-radius: 15px;\n"
"font-size: 30px;\n"
"font-family: Tempus Sans ITC\n"
"}\n"
"\n"
"#btn_close{\n"
"font-size: 24px;\n"
"}")
        self.btn_close = QtWidgets.QPushButton(alphaPg)
        self.btn_close.setGeometry(QtCore.QRect(280, 540, 89, 25))
        self.btn_close.setMinimumSize(QtCore.QSize(89, 25))
        self.btn_close.setMaximumSize(QtCore.QSize(89, 25))
        self.btn_close.setObjectName("btn_close")
        self.scrollArea = QtWidgets.QScrollArea(alphaPg)
        self.scrollArea.setGeometry(QtCore.QRect(50, 80, 591, 441))
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 589, 439))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label = QtWidgets.QLabel(alphaPg)
        self.label.setGeometry(QtCore.QRect(66, 10, 561, 61))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(alphaPg)
        self.btn_close.clicked.connect(alphaPg.close)
        QtCore.QMetaObject.connectSlotsByName(alphaPg)

    def retranslateUi(self, alphaPg):
        _translate = QtCore.QCoreApplication.translate
        alphaPg.setWindowTitle(_translate("alphaPg", "Select letter"))
        self.btn_close.setText(_translate("alphaPg", "Close"))
        self.label.setText(_translate("alphaPg", "Select a letter to view"))

