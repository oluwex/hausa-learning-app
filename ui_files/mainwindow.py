# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Habeeb\Documents\Pycharm Projects\Hausa project\ui_files\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(831, 680)
        MainWindow.setStyleSheet("#label{\n"
"border: 2px solid gray;\n"
"border-radius: 10px;\n"
"background-color: beige;\n"
"padding:2px;\n"
"font-size: 40px;\n"
"font-family: Tempus Sans ITC;\n"
"}\n"
"\n"
"#pixDisp{\n"
"font: 245px Calibri;\n"
"color: brown\n"
"}\n"
"\n"
"#itemDisp{\n"
"font-size: 27px;\n"
"font-family: Calibri;\n"
"color: brown;\n"
"padding:2px;\n"
"}\n"
"\n"
"#btn_next{\n"
"image: url(:/icons/images/arrow-right.png);\n"
"border: none\n"
"}\n"
"\n"
"#btn_previous{\n"
"image: url(:/icons/images/arrow-left.png);\n"
"border: none\n"
"}\n"
"\n"
"#btn_next:hover, #btn_previous:hover{\n"
"background-color: lightgrey;\n"
"}\n"
"\n"
"#btn_next:pressed, #btn_previous:pressed{\n"
"background-color: lightslategray;\n"
"}\n"
"\n"
"QListWidget{\n"
"font-family: calibri;\n"
"font-size: 16px;\n"
"border: 1px solid lightgray;\n"
"padding: 3px\n"
"}\n"
"\n"
"#label_example{\n"
"padding: 1px;\n"
"font: 19px Calibri;\n"
"}\n"
"\n"
"#btn_speak{\n"
"border:none;\n"
"}\n"
"\n"
"#word_1,#word_2,#word_3,#word_4{\n"
"border: none\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 139, 781, 481))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.pixDisp = QtWidgets.QLabel(self.widget)
        self.pixDisp.setGeometry(QtCore.QRect(210, 30, 391, 311))
        self.pixDisp.setText("")
        self.pixDisp.setPixmap(QtGui.QPixmap(":/icons/images/blank.png"))
        self.pixDisp.setScaledContents(True)
        self.pixDisp.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.pixDisp.setObjectName("pixDisp")
        self.btn_next = QtWidgets.QPushButton(self.widget)
        self.btn_next.setGeometry(QtCore.QRect(650, 210, 75, 51))
        self.btn_next.setText("")
        self.btn_next.setObjectName("btn_next")
        self.btn_previous = QtWidgets.QPushButton(self.widget)
        self.btn_previous.setGeometry(QtCore.QRect(50, 210, 75, 51))
        self.btn_previous.setText("")
        self.btn_previous.setObjectName("btn_previous")
        self.itemDisp = QtWidgets.QLabel(self.widget)
        self.itemDisp.setGeometry(QtCore.QRect(180, 340, 451, 59))
        self.itemDisp.setText("")
        self.itemDisp.setTextFormat(QtCore.Qt.RichText)
        self.itemDisp.setScaledContents(True)
        self.itemDisp.setAlignment(QtCore.Qt.AlignCenter)
        self.itemDisp.setObjectName("itemDisp")
        self.label_example = QtWidgets.QLabel(self.widget)
        self.label_example.setGeometry(QtCore.QRect(120, 430, 621, 31))
        self.label_example.setText("")
        self.label_example.setObjectName("label_example")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 10, 751, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(68, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(501, 101))
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_chooseAlpha = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_chooseAlpha.sizePolicy().hasHeightForWidth())
        self.btn_chooseAlpha.setSizePolicy(sizePolicy)
        self.btn_chooseAlpha.setMinimumSize(QtCore.QSize(135, 23))
        self.btn_chooseAlpha.setStyleSheet("border: 2px solid gray;\n"
"border-radius: 5px;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c);\n"
"padding:2px;\n"
"font-family: calibri;\n"
"font-size: 13px;\n"
"width:90px")
        self.btn_chooseAlpha.setObjectName("btn_chooseAlpha")
        self.verticalLayout.addWidget(self.btn_chooseAlpha)
        self.btn_goBack = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_goBack.sizePolicy().hasHeightForWidth())
        self.btn_goBack.setSizePolicy(sizePolicy)
        self.btn_goBack.setMinimumSize(QtCore.QSize(135, 23))
        self.btn_goBack.setStyleSheet("border: 2px solid gray;\n"
"border-radius: 5px;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c);\n"
"padding:2px;\n"
"font-family: calibri;\n"
"font-size: 13px;\n"
"width:90px")
        self.btn_goBack.setText("")
        self.btn_goBack.setObjectName("btn_goBack")
        self.verticalLayout.addWidget(self.btn_goBack)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(22, 24))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menu = QtWidgets.QMenuBar(MainWindow)
        self.menu.setGeometry(QtCore.QRect(0, 0, 831, 21))
        self.menu.setObjectName("menu")
        self.menuActions = QtWidgets.QMenu(self.menu)
        self.menuActions.setObjectName("menuActions")
        MainWindow.setMenuBar(self.menu)
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon)
        self.actionExit.setObjectName("actionExit")
        self.actionRemove = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/remove_user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemove.setIcon(icon1)
        self.actionRemove.setObjectName("actionRemove")
        self.actionEdit = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/edit_user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit.setIcon(icon2)
        self.actionEdit.setObjectName("actionEdit")
        self.actionAdd_Word = QtWidgets.QAction(MainWindow)
        self.actionAdd_Word.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/images/add-notes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_Word.setIcon(icon3)
        self.actionAdd_Word.setVisible(False)
        self.actionAdd_Word.setObjectName("actionAdd_Word")
        self.actionEdit_Word = QtWidgets.QAction(MainWindow)
        self.actionEdit_Word.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/images/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit_Word.setIcon(icon4)
        self.actionEdit_Word.setVisible(False)
        self.actionEdit_Word.setObjectName("actionEdit_Word")
        self.actionRemove_word = QtWidgets.QAction(MainWindow)
        self.actionRemove_word.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/images/delete-file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemove_word.setIcon(icon5)
        self.actionRemove_word.setVisible(False)
        self.actionRemove_word.setObjectName("actionRemove_word")
        self.actionHistory = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/images/history.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHistory.setIcon(icon6)
        self.actionHistory.setObjectName("actionHistory")
        self.actionLogout = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/images/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLogout.setIcon(icon7)
        self.actionLogout.setObjectName("actionLogout")
        self.actionAdd_new_user = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/images/add_user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_new_user.setIcon(icon8)
        self.actionAdd_new_user.setVisible(False)
        self.actionAdd_new_user.setObjectName("actionAdd_new_user")
        self.actionUser = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/images/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUser.setIcon(icon9)
        self.actionUser.setObjectName("actionUser")
        self.actionView_users = QtWidgets.QAction(MainWindow)
        self.actionView_users.setObjectName("actionView_users")
        self.actionView_admin = QtWidgets.QAction(MainWindow)
        self.actionView_admin.setObjectName("actionView_admin")
        self.toolBar.addAction(self.actionUser)
        self.toolBar.addAction(self.actionEdit)
        self.toolBar.addAction(self.actionRemove)
        self.toolBar.addAction(self.actionAdd_new_user)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionHistory)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAdd_Word)
        self.toolBar.addAction(self.actionEdit_Word)
        self.toolBar.addAction(self.actionRemove_word)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionLogout)
        self.toolBar.addAction(self.actionExit)
        self.toolBar.addSeparator()
        self.menuActions.addAction(self.actionView_users)
        self.menuActions.addAction(self.actionView_admin)
        self.menu.addAction(self.menuActions.menuAction())

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hausa Learning App"))
        self.btn_chooseAlpha.setText(_translate("MainWindow", "Choose alphabet"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.menuActions.setTitle(_translate("MainWindow", "Actions"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionRemove.setText(_translate("MainWindow", "Remove"))
        self.actionRemove.setToolTip(_translate("MainWindow", "Remove Profile"))
        self.actionEdit.setText(_translate("MainWindow", "Edit"))
        self.actionEdit.setToolTip(_translate("MainWindow", "Edit Profile"))
        self.actionAdd_Word.setText(_translate("MainWindow", "Add Word"))
        self.actionAdd_Word.setToolTip(_translate("MainWindow", "Click to add word"))
        self.actionEdit_Word.setText(_translate("MainWindow", "Edit Word"))
        self.actionEdit_Word.setToolTip(_translate("MainWindow", "Click to edit the word entry"))
        self.actionRemove_word.setText(_translate("MainWindow", "Remove word"))
        self.actionRemove_word.setToolTip(_translate("MainWindow", "Click to remove the selected word"))
        self.actionHistory.setText(_translate("MainWindow", "History"))
        self.actionHistory.setToolTip(_translate("MainWindow", "Click to see your view history"))
        self.actionLogout.setText(_translate("MainWindow", "Switch User"))
        self.actionLogout.setToolTip(_translate("MainWindow", "Click to logout"))
        self.actionAdd_new_user.setText(_translate("MainWindow", "Add new user"))
        self.actionAdd_new_user.setToolTip(_translate("MainWindow", "Click to add new admin"))
        self.actionUser.setText(_translate("MainWindow", "User"))
        self.actionView_users.setText(_translate("MainWindow", "View users"))
        self.actionView_admin.setText(_translate("MainWindow", "View administrators"))

from ui_files import hausa_app_rc
