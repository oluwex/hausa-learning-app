# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Habeeb\Documents\Pycharm Projects\Hausa project\ui_files\signup.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.resize(477, 501)
        Form.setStyleSheet("#frame{\n"
"border: 3px solid gray;\n"
"background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #eef, stop: 1 #ccf);\n"
"border-radius: 40px\n"
"}\n"
"\n"
"QLineEdit{\n"
"padding: 2px;\n"
"border: 2px solid gray;\n"
"border-radius: 9px\n"
"}\n"
"\n"
"QLabel{\n"
"font-weight: bold;\n"
"font-size: 12px\n"
"}\n"
"\n"
"QPushButton{\n"
"border: 1px solid grey;\n"
"border-radius: 6px;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c);\n"
"padding: 2px;\n"
"}")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(40, 30, 401, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(50, -1, 50, -1)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.fname = QtWidgets.QLineEdit(self.frame)
        self.fname.setMinimumSize(QtCore.QSize(191, 27))
        self.fname.setObjectName("fname")
        self.gridLayout.addWidget(self.fname, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.mname = QtWidgets.QLineEdit(self.frame)
        self.mname.setMinimumSize(QtCore.QSize(191, 27))
        self.mname.setObjectName("mname")
        self.gridLayout.addWidget(self.mname, 1, 2, 1, 1)
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setMinimumSize(QtCore.QSize(191, 27))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 4, 2, 1, 1)
        self.lname = QtWidgets.QLineEdit(self.frame)
        self.lname.setMinimumSize(QtCore.QSize(191, 27))
        self.lname.setObjectName("lname")
        self.gridLayout.addWidget(self.lname, 2, 2, 1, 1)
        self.username = QtWidgets.QLineEdit(self.frame)
        self.username.setMinimumSize(QtCore.QSize(191, 27))
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 3, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 2)
        self.btn_submit = QtWidgets.QPushButton(self.frame)
        self.btn_submit.setMinimumSize(QtCore.QSize(75, 23))
        self.btn_submit.setMaximumSize(QtCore.QSize(75, 23))
        self.btn_submit.setObjectName("btn_submit")
        self.gridLayout.addWidget(self.btn_submit, 5, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.fname, self.mname)
        Form.setTabOrder(self.mname, self.lname)
        Form.setTabOrder(self.lname, self.username)
        Form.setTabOrder(self.username, self.password)
        Form.setTabOrder(self.password, self.btn_submit)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sign Up"))
        self.fname.setPlaceholderText(_translate("Form", "Enter your first name"))
        self.label.setText(_translate("Form", "First Name:"))
        self.label_3.setText(_translate("Form", "Last Name:"))
        self.label_2.setText(_translate("Form", "Middle Name:"))
        self.mname.setPlaceholderText(_translate("Form", "Enter your middle name"))
        self.password.setToolTip(_translate("Form", "Should not be less than 3 characters long"))
        self.password.setPlaceholderText(_translate("Form", "Enter your password"))
        self.lname.setPlaceholderText(_translate("Form", "Enter your last name"))
        self.username.setPlaceholderText(_translate("Form", "Enter your preferred username"))
        self.label_5.setText(_translate("Form", "Password:"))
        self.label_4.setText(_translate("Form", "Username:"))
        self.btn_submit.setText(_translate("Form", "Submit"))

