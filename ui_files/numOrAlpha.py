# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Habeeb\Documents\Pycharm Projects\Hausa project\ui_files\numOrAlpha.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(654, 531)
        Dialog.setStyleSheet("QPushButton{\n"
"background-color: gray;\n"
"border: 2px solid gray;\n"
"border-radius: 15px;\n"
"font-size: 30px;\n"
"font-family: Tempus Sans ITC\n"
"}\n"
"\n"
"QLabel{\n"
"font-size: 25px;\n"
"font-family: Tempus Sans ITC\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c);\n"
"}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(290, 270, 81, 81))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(320, 140, 20, 121))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(320, 370, 20, 121))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 591, 101))
        self.label_2.setMinimumSize(QtCore.QSize(591, 101))
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.frame1 = QtWidgets.QFrame(Dialog)
        self.frame1.setGeometry(QtCore.QRect(9, 129, 271, 401))
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.btn_alpha = QtWidgets.QPushButton(self.frame1)
        self.btn_alpha.setGeometry(QtCore.QRect(40, 80, 221, 201))
        self.btn_alpha.setMinimumSize(QtCore.QSize(221, 201))
        self.btn_alpha.setObjectName("btn_alpha")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(379, 129, 271, 401))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_number = QtWidgets.QPushButton(self.frame)
        self.btn_number.setGeometry(QtCore.QRect(20, 80, 221, 201))
        self.btn_number.setMinimumSize(QtCore.QSize(221, 201))
        self.btn_number.setObjectName("btn_number")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Make a choice"))
        self.label.setText(_translate("Dialog", "Or"))
        self.btn_alpha.setText(_translate("Dialog", "Alphabets"))
        self.btn_number.setText(_translate("Dialog", "Numbers"))

