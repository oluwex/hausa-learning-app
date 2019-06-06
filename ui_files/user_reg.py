# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Habeeb\Documents\Pycharm Projects\Hausa project\ui_files\user_reg.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(322, 150)
        Dialog.setMinimumSize(QtCore.QSize(322, 150))
        Dialog.setMaximumSize(QtCore.QSize(322, 150))
        Dialog.setStyleSheet("QLineEdit{\n"
"padding: 2px;\n"
"border: 3px solid gray;\n"
"border-radius: 9px;\n"
"}\n"
"\n"
"QLabel{\n"
"font-family: calibri;\n"
"font-weight: bold;\n"
"font-size: 14px\n"
"}\n"
"\n"
"QPushButton{\n"
"border: 1px solid grey;\n"
"border-radius: 6px;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c);\n"
"padding: 2px;\n"
"height: 20px;\n"
"width: 70px\n"
"}")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-60, 100, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.name = QtWidgets.QLineEdit(Dialog)
        self.name.setGeometry(QtCore.QRect(40, 50, 241, 41))
        self.name.setClearButtonEnabled(True)
        self.name.setObjectName("name")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 25, 191, 21))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Create a profile"))
        self.label.setText(_translate("Dialog", "Enter your username"))

