# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Habeeb\Documents\Pycharm Projects\Hausa project\ui_files\addWord.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(582, 589)
        Form.setStyleSheet("QLineEdit, QTextEdit{\n"
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
"#disp{\n"
"border: 2px solid gray;\n"
"border-radius: 10px;\n"
"background-color: beige;\n"
"padding:2px;\n"
"font-size: 25px;\n"
"font-family: Tempus Sans ITC;\n"
"}\n"
"\n"
"QPushButton{\n"
"border: 1px solid grey;\n"
"border-radius: 6px;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c);\n"
"padding: 2px;\n"
"width: 50px;\n"
"}")
        self.disp = QtWidgets.QLabel(Form)
        self.disp.setGeometry(QtCore.QRect(150, 20, 261, 111))
        self.disp.setTextFormat(QtCore.Qt.RichText)
        self.disp.setAlignment(QtCore.Qt.AlignCenter)
        self.disp.setObjectName("disp")
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setGeometry(QtCore.QRect(370, 520, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 150, 444, 311))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.hWord = QtWidgets.QLineEdit(self.layoutWidget)
        self.hWord.setMinimumSize(QtCore.QSize(256, 30))
        self.hWord.setClearButtonEnabled(True)
        self.hWord.setObjectName("hWord")
        self.gridLayout.addWidget(self.hWord, 0, 1, 1, 1)
        self.eWord = QtWidgets.QLineEdit(self.layoutWidget)
        self.eWord.setMinimumSize(QtCore.QSize(256, 30))
        self.eWord.setClearButtonEnabled(True)
        self.eWord.setObjectName("eWord")
        self.gridLayout.addWidget(self.eWord, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.hExample = QtWidgets.QTextEdit(self.layoutWidget)
        self.hExample.setMaximumSize(QtCore.QSize(256, 70))
        self.hExample.setObjectName("hExample")
        self.gridLayout.addWidget(self.hExample, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.eExample = QtWidgets.QTextEdit(self.layoutWidget)
        self.eExample.setMinimumSize(QtCore.QSize(256, 70))
        self.eExample.setMaximumSize(QtCore.QSize(256, 70))
        self.eExample.setObjectName("eExample")
        self.gridLayout.addWidget(self.eExample, 3, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(130, 470, 276, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.imageFileName = QtWidgets.QLineEdit(self.layoutWidget1)
        self.imageFileName.setObjectName("imageFileName")
        self.horizontalLayout.addWidget(self.imageFileName)
        self.btn_browse = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_browse.setObjectName("btn_browse")
        self.horizontalLayout.addWidget(self.btn_browse)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.disp.setText(_translate("Form", "Add Word"))
        self.label.setText(_translate("Form", "Hausa word"))
        self.label_3.setText(_translate("Form", "Hausa example sentence"))
        self.label_2.setText(_translate("Form", "English gloss"))
        self.label_4.setText(_translate("Form", "English example sentence"))
        self.label_5.setText(_translate("Form", "Select Picture: "))
        self.btn_browse.setText(_translate("Form", "Browse"))

