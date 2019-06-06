# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Habeeb\Documents\Pycharm Projects\Hausa project\ui_files\history.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(471, 401)
        Dialog.setStyleSheet("QTableView::cell{\n"
"text-align: center;\n"
"padding: 4px;\n"
"}")
        self.btn_close = QtWidgets.QPushButton(Dialog)
        self.btn_close.setGeometry(QtCore.QRect(200, 360, 75, 23))
        self.btn_close.setObjectName("btn_close")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(30, 41, 411, 311))
        self.tableView.setShowGrid(False)
        self.tableView.setCornerButtonEnabled(False)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setHighlightSections(False)
        self.tableView.horizontalHeader().setStretchLastSection(True)

        self.retranslateUi(Dialog)
        self.btn_close.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "View History"))
        self.btn_close.setText(_translate("Dialog", "Close"))

