# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Habeeb\Documents\Pycharm Projects\Hausa project\ui_files\selectUser.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(560, 592)
        Dialog.setMinimumSize(QtCore.QSize(560, 592))
        Dialog.setMaximumSize(QtCore.QSize(560, 592))
        Dialog.setStyleSheet("QPushButton{\n"
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
"font-size: 17px;\n"
"}\n"
"\n"
"QListWidget{\n"
"border: none;\n"
"font-family: calibri;\n"
"font-size: 14px;\n"
"}")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(13, 56, 421, 461))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("")
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
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(443, 106, 111, 181))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_new = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_new.setMinimumSize(QtCore.QSize(90, 23))
        self.btn_new.setMaximumSize(QtCore.QSize(90, 23))
        self.btn_new.setObjectName("btn_new")
        self.verticalLayout.addWidget(self.btn_new)
        self.btn_edit = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_edit.setEnabled(False)
        self.btn_edit.setMinimumSize(QtCore.QSize(90, 23))
        self.btn_edit.setMaximumSize(QtCore.QSize(90, 23))
        self.btn_edit.setObjectName("btn_edit")
        self.verticalLayout.addWidget(self.btn_edit)
        self.btn_remove = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_remove.setEnabled(False)
        self.btn_remove.setMinimumSize(QtCore.QSize(90, 23))
        self.btn_remove.setMaximumSize(QtCore.QSize(90, 23))
        self.btn_remove.setObjectName("btn_remove")
        self.verticalLayout.addWidget(self.btn_remove)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(13, 26, 401, 21))
        self.label.setObjectName("label")
        self.layoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(160, 520, 271, 41))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_continue = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btn_continue.setEnabled(False)
        self.btn_continue.setMinimumSize(QtCore.QSize(102, 23))
        self.btn_continue.setMaximumSize(QtCore.QSize(102, 23))
        self.btn_continue.setObjectName("btn_continue")
        self.horizontalLayout.addWidget(self.btn_continue)
        self.btn_exit = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btn_exit.setMinimumSize(QtCore.QSize(101, 23))
        self.btn_exit.setMaximumSize(QtCore.QSize(101, 23))
        self.btn_exit.setObjectName("btn_exit")
        self.horizontalLayout.addWidget(self.btn_exit)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.btn_continue.clicked.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Choose user"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Users"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Displays the list of normal users"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Admin"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Displays the list of admin users"))
        self.btn_new.setText(_translate("Dialog", "New User"))
        self.btn_edit.setText(_translate("Dialog", "Edit User"))
        self.btn_remove.setText(_translate("Dialog", "Remove User"))
        self.label.setText(_translate("Dialog", "Select your profile from the appropriate user type below"))
        self.btn_continue.setText(_translate("Dialog", "Continue"))
        self.btn_exit.setText(_translate("Dialog", "Exit"))

