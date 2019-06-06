# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Habeeb\Documents\Pycharm Projects\Hausa project\ui_files\login.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.setMaximumSize(QtCore.QSize(356, 290))
        Dialog.setStyleSheet("QLineEdit{\n"
"padding: 2px;\n"
"border: 2px solid gray;\n"
"border-radius: 9px\n"
"}\n"
"\n"
"QLabel{\n"
"font-family: calibri;\n"
"font-weight: bold;\n"
"font-size: 14px\n"
"}\n"
"\n"
"#label_3{\n"
"font-size: 12px\n"
"}\n"
"\n"
"QPushButton{\n"
"border: 1px solid grey;\n"
"border-radius: 6px;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c);\n"
"padding: 2px;\n"
"}")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 274, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(65, 34))
        self.label_2.setMaximumSize(QtCore.QSize(65, 24))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(self.layoutWidget)
        self.password.setMinimumSize(QtCore.QSize(133, 24))
        self.password.setMaximumSize(QtCore.QSize(133, 24))
        self.password.setInputMask("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(65, 24))
        self.label.setMaximumSize(QtCore.QSize(65, 24))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.userName = QtWidgets.QLabel(self.layoutWidget)
        self.userName.setMinimumSize(QtCore.QSize(133, 24))
        self.userName.setMaximumSize(QtCore.QSize(133, 24))
        self.userName.setText("")
        self.userName.setObjectName("userName")
        self.gridLayout.addWidget(self.userName, 0, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(130, 150, 181, 51))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_login = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_login.setMinimumSize(QtCore.QSize(70, 23))
        self.btn_login.setMaximumSize(QtCore.QSize(70, 23))
        self.btn_login.setObjectName("btn_login")
        self.horizontalLayout.addWidget(self.btn_login)
        self.btn_cancel = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_cancel.setMinimumSize(QtCore.QSize(70, 23))
        self.btn_cancel.setMaximumSize(QtCore.QSize(70, 23))
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)

        self.retranslateUi(Dialog)
        self.btn_cancel.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.label_2.setText(_translate("Dialog", "Password:"))
        self.password.setPlaceholderText(_translate("Dialog", "Enter your password"))
        self.label.setText(_translate("Dialog", "Username:"))
        self.btn_login.setText(_translate("Dialog", "Login"))
        self.btn_cancel.setText(_translate("Dialog", "Cancel"))

