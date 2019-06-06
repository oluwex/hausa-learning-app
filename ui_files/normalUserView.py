# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Habeeb\Documents\Pycharm Projects\Hausa project\ui_files\normalUserView.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(610, 560)
        Dialog.setStyleSheet("QComboBox{\n"
"font: 14px Calibri\n"
"}\n"
"\n"
"QGroupBox{\n"
"font-size: 12px\n"
"}")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 30, 218, 45))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(490, 520, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(39, 100, 531, 411))
        self.groupBox_2.setObjectName("groupBox_2")
        self.alphaBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.alphaBox.setGeometry(QtCore.QRect(10, 30, 261, 361))
        self.alphaBox.setObjectName("alphaBox")
        self.alphaTable = QtWidgets.QTableView(self.alphaBox)
        self.alphaTable.setGeometry(QtCore.QRect(15, 20, 231, 281))
        self.alphaTable.setObjectName("alphaTable")
        self.label_2 = QtWidgets.QLabel(self.alphaBox)
        self.label_2.setGeometry(QtCore.QRect(20, 310, 111, 32))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.alphaBox)
        self.label_3.setGeometry(QtCore.QRect(130, 310, 131, 31))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox.setGeometry(QtCore.QRect(310, 30, 211, 361))
        self.groupBox.setObjectName("groupBox")
        self.numberTable = QtWidgets.QTableView(self.groupBox)
        self.numberTable.setGeometry(QtCore.QRect(10, 20, 191, 281))
        self.numberTable.setObjectName("numberTable")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 310, 111, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(120, 310, 71, 31))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "History"))
        self.label.setText(_translate("Dialog", "Select User to view"))
        self.pushButton.setText(_translate("Dialog", "Done"))
        self.groupBox_2.setTitle(_translate("Dialog", "User History"))
        self.alphaBox.setTitle(_translate("Dialog", "Alphabets Viewed"))
        self.label_2.setText(_translate("Dialog", "Percentage Complete"))
        self.groupBox.setTitle(_translate("Dialog", "Numbers Viewed"))
        self.label_4.setText(_translate("Dialog", "Percentage Complete"))

