# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Habeeb\Documents\Pycharm Projects\Hausa project\ui_files\choose_user.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(560, 592)
        Form.setMinimumSize(QtCore.QSize(560, 592))
        Form.setMaximumSize(QtCore.QSize(560, 592))
        Form.setStyleSheet("QPushButton{\n"
"border: 2px solid gray;\n"
"border-radius: 5px;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c);\n"
"padding:2px;\n"
"font-family: calibri;\n"
"font-size: 13px\n"
"}\n"
"\n"
"QLabel{\n"
"font-family: calibri;\n"
"font-size: 13px;\n"
"}\n"
"\n"
"QListWidget{\n"
"font-family: calibri;\n"
"font-size: 14px;\n"
"}\n"
"\n"
"QTabBar:: tab{\n"
"border: 1px solid;\n"
"border-radius: 3px\n"
"}\n"
"\n"
"")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 30, 371, 21))
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 60, 421, 461))
        self.tabWidget.setStyleSheet("QTabBar::tab{\n"
"background-color: lightgray;\n"
"border: 1px solid gray;\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 3px;\n"
"padding: 4px;\n"
"width: 40px\n"
"}\n"
"\n"
"QTabBar::tab:selected{\n"
"background-color: white;\n"
"border: 1px solid gray;\n"
"border-top-left-radius: 8px;\n"
"padding: 4px;\n"
"width: 40px\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.userList = QtWidgets.QListWidget(self.tab)
        self.userList.setGeometry(QtCore.QRect(0, 1, 411, 431))
        self.userList.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.SelectedClicked)
        self.userList.setAlternatingRowColors(True)
        self.userList.setObjectName("userList")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.adminList = QtWidgets.QListWidget(self.tab_2)
        self.adminList.setGeometry(QtCore.QRect(0, 0, 411, 441))
        self.adminList.setObjectName("adminList")
        self.tabWidget.addTab(self.tab_2, "")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(157, 524, 271, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_continue = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_continue.setEnabled(False)
        self.btn_continue.setMinimumSize(QtCore.QSize(102, 23))
        self.btn_continue.setMaximumSize(QtCore.QSize(102, 23))
        self.btn_continue.setObjectName("btn_continue")
        self.horizontalLayout.addWidget(self.btn_continue)
        self.btn_exit = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_exit.setMinimumSize(QtCore.QSize(101, 23))
        self.btn_exit.setMaximumSize(QtCore.QSize(101, 23))
        self.btn_exit.setObjectName("btn_exit")
        self.horizontalLayout.addWidget(self.btn_exit)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(440, 110, 111, 181))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_new = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_new.setMinimumSize(QtCore.QSize(90, 23))
        self.btn_new.setMaximumSize(QtCore.QSize(90, 23))
        self.btn_new.setObjectName("btn_new")
        self.verticalLayout.addWidget(self.btn_new)
        self.btn_edit = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_edit.setEnabled(False)
        self.btn_edit.setMinimumSize(QtCore.QSize(90, 23))
        self.btn_edit.setMaximumSize(QtCore.QSize(90, 23))
        self.btn_edit.setObjectName("btn_edit")
        self.verticalLayout.addWidget(self.btn_edit)
        self.btn_remove = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_remove.setEnabled(False)
        self.btn_remove.setMinimumSize(QtCore.QSize(90, 23))
        self.btn_remove.setMaximumSize(QtCore.QSize(90, 23))
        self.btn_remove.setObjectName("btn_remove")
        self.verticalLayout.addWidget(self.btn_remove)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.btn_exit.clicked.connect(Form.close)
        self.btn_continue.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Choose User"))
        self.label.setText(_translate("Form", "Select your profile from the appropriate user type below"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Users"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab), _translate("Form", "Displays the list of normal users"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Admin"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Displays the list of admin users"))
        self.btn_continue.setText(_translate("Form", "Continue"))
        self.btn_exit.setText(_translate("Form", "Exit"))
        self.btn_new.setText(_translate("Form", "New User"))
        self.btn_edit.setText(_translate("Form", "Edit User"))
        self.btn_remove.setText(_translate("Form", "Remove User"))

